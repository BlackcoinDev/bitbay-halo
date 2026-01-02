"""
Threading module for BlackHalo 2.0
Type-safe background worker threads and thread pool management
"""

from typing import Any, Callable, Dict, List, Optional, Protocol, runtime_checkable
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from concurrent.futures import ThreadPoolExecutor, Future
from threading import Thread, Lock, Condition, Event
from abc import ABC, abstractmethod
import logging
import uuid
import time


logger = logging.getLogger(__name__)


class ThreadState(Enum):
    """Thread lifecycle state"""

    CREATED = "created"
    STARTING = "starting"
    RUNNING = "running"
    STOPPING = "stopping"
    STOPPED = "stopped"
    FAILED = "failed"


class TaskPriority(Enum):
    """Task execution priority"""

    LOW = 0
    NORMAL = 1
    HIGH = 2
    CRITICAL = 3


@dataclass
class Task:
    """Background task definition"""

    task_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    func: Optional[Callable[..., Any]] = None
    args: tuple = field(default_factory=tuple)
    kwargs: Dict[str, Any] = field(default_factory=dict)
    priority: TaskPriority = TaskPriority.NORMAL
    created_at: datetime = field(default_factory=datetime.utcnow)
    state: ThreadState = ThreadState.CREATED
    error: Optional[str] = None
    result: Any = None

    def execute(self) -> Any:
        """Execute the task"""
        if self.func is not None:
            self.state = ThreadState.RUNNING
            try:
                self.result = self.func(*self.args, **self.kwargs)
                return self.result
            except Exception as e:
                self.error = str(e)
                self.state = ThreadState.FAILED
                raise
        return None


@dataclass
class ThreadInfo:
    """Information about a running thread"""

    thread_id: int
    name: str
    state: ThreadState
    is_daemon: bool = False
    start_time: Optional[datetime] = None
    last_activity: Optional[datetime] = None
    iterations: int = 0
    error: Optional[str] = None


class IWorker(Protocol):
    """Protocol for worker thread interface"""

    @property
    def name(self) -> str: ...
    @property
    def state(self) -> ThreadState: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def is_running(self) -> bool: ...
    def join(self, timeout: Optional[float] = None) -> None: ...


class WorkerThread(Thread):
    """
    Base worker thread with state management.
    Provides start/stop/join functionality with proper synchronization.
    """

    def __init__(
        self,
        name: str,
        is_daemon: bool = False,
        target: Optional[Callable[..., Any]] = None,
        args: tuple = (),
        kwargs: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize worker thread"""
        super().__init__(name=name, daemon=is_daemon)
        self._name = name
        self._is_daemon = is_daemon
        self._target = target
        self._args = args
        self._kwargs = kwargs or {}
        self._state = ThreadState.CREATED
        self._stop_event = Event()
        self._pause_event = Event()
        self._pause_event.set()
        self._lock = Lock()
        self._error: Optional[str] = None
        self._start_time: Optional[datetime] = None
        self._last_activity: Optional[datetime] = None
        self._iterations = 0

    @property
    def name(self) -> str:
        """Get thread name"""
        return self._name

    @property
    def state(self) -> ThreadState:
        """Get thread state"""
        return self._state

    @property
    def is_daemon(self) -> bool:
        """Check if daemon thread"""
        return self._is_daemon

    @property
    def error(self) -> Optional[str]:
        """Get last error"""
        return self._error

    def start(self) -> None:
        """Start the thread"""
        with self._lock:
            if self._state == ThreadState.RUNNING:
                return
            self._state = ThreadState.STARTING
            self._stop_event.clear()
            super().start()
            self._start_time = datetime.utcnow()

    def stop(self, timeout: float = 5.0) -> None:
        """Stop the thread"""
        with self._lock:
            if self._state == ThreadState.STOPPED:
                return
            self._state = ThreadState.STOPPING
            self._stop_event.set()
        self.join(timeout=timeout)
        if self.is_alive():
            logger.warning(f"Thread {self._name} did not stop gracefully")

    def pause(self) -> None:
        """Pause the thread"""
        self._pause_event.clear()

    def resume(self) -> None:
        """Resume the thread"""
        self._pause_event.set()

    def is_running(self) -> bool:
        """Check if thread is running"""
        return self._state == ThreadState.RUNNING and self.is_alive()

    def should_stop(self) -> bool:
        """Check if stop was requested"""
        return self._stop_event.is_set()

    def should_pause(self) -> bool:
        """Check if pause was requested"""
        return not self._pause_event.is_set()

    def run(self) -> None:
        """Thread main loop"""
        try:
            self._state = ThreadState.RUNNING
            if self._target is not None:
                self._target(*self._args, **self._kwargs)
            else:
                self._main_loop()
        except Exception as e:
            self._error = str(e)
            self._state = ThreadState.FAILED
            logger.error(f"Thread {self._name} failed: {e}")
        finally:
            self._state = ThreadState.STOPPED

    def _main_loop(self) -> None:
        """Override this method for custom thread logic"""
        while not self.should_stop():
            self._pause_event.wait()
            if self.should_stop():
                break
            time.sleep(0.1)
            self._iterations += 1
            self._last_activity = datetime.utcnow()

    def get_info(self) -> ThreadInfo:
        """Get thread information"""
        return ThreadInfo(
            thread_id=self.ident or 0,
            name=self._name,
            state=self._state,
            is_daemon=self._is_daemon,
            start_time=self._start_time,
            last_activity=self._last_activity,
            iterations=self._iterations,
            error=self._error,
        )

    def join(self, timeout: Optional[float] = None) -> None:
        """Wait for thread to complete"""
        try:
            super().join(timeout=timeout)
        except RuntimeError:
            pass


class PeriodicWorker(WorkerThread):
    """Worker thread that executes at regular intervals"""

    def __init__(
        self,
        name: str,
        interval: float,
        is_daemon: bool = True,
        target: Optional[Callable[..., Any]] = None,
        args: tuple = (),
        kwargs: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize periodic worker"""
        super().__init__(
            name=name, is_daemon=is_daemon, target=target, args=args, kwargs=kwargs
        )
        self._interval = interval
        self._last_run: Optional[datetime] = None

    @property
    def interval(self) -> float:
        """Get execution interval in seconds"""
        return self._interval

    def _main_loop(self) -> None:
        """Main loop with periodic execution"""
        while not self.should_stop():
            self._pause_event.wait()
            if self.should_stop():
                break

            try:
                if self._target is not None:
                    self._target(*self._args, **self._kwargs)
                else:
                    self._execute_task()
            except Exception as e:
                self._error = str(e)
                logger.error(f"Periodic worker {self._name} error: {e}")

            self._last_run = datetime.utcnow()
            self._iterations += 1

            for _ in range(int(self._interval * 10)):
                if self.should_stop() or not self._pause_event.is_set():
                    break
                time.sleep(0.1)

    def _execute_task(self) -> None:
        """Override for custom task execution"""
        pass

    def get_last_run(self) -> Optional[datetime]:
        """Get last execution time"""
        return self._last_run


class ThreadPoolManager:
    """
    Thread pool manager for managing worker threads.
    Provides task scheduling and thread lifecycle management.
    """

    def __init__(
        self,
        max_workers: int = 4,
        thread_prefix: str = "BlackHalo",
    ) -> None:
        """Initialize thread pool manager"""
        self._max_workers = max_workers
        self._thread_prefix = thread_prefix
        self._executor = ThreadPoolExecutor(
            max_workers=max_workers, thread_name_prefix=thread_prefix
        )
        self._workers: List[WorkerThread] = []
        self._worker_lock = Lock()
        self._running = False
        self._task_queue: List[Task] = []
        self._queue_lock = Lock()

    @property
    def max_workers(self) -> int:
        """Get maximum number of workers"""
        return self._max_workers

    @property
    def active_count(self) -> int:
        """Get number of active threads"""
        return sum(1 for w in self._workers if w.is_running())

    def submit_task(
        self,
        func: Callable[..., Any],
        *args: Any,
        priority: TaskPriority = TaskPriority.NORMAL,
        **kwargs: Any,
    ) -> Future:
        """Submit task to thread pool"""
        task = Task(
            name=f"task-{uuid.uuid4().hex[:8]}",
            func=func,
            args=args,
            kwargs=kwargs,
            priority=priority,
        )
        return self._executor.submit(task.execute)

    def create_worker(
        self,
        name: str,
        target: Callable[..., Any],
        args: tuple = (),
        is_daemon: bool = True,
    ) -> WorkerThread:
        """Create and register a worker thread"""
        worker = WorkerThread(
            name=f"{self._thread_prefix}-{name}",
            is_daemon=is_daemon,
            target=target,
            args=args,
        )
        with self._worker_lock:
            self._workers.append(worker)
        return worker

    def create_periodic_worker(
        self,
        name: str,
        interval: float,
        target: Callable[..., Any],
        args: tuple = (),
        is_daemon: bool = True,
    ) -> PeriodicWorker:
        """Create and register a periodic worker"""
        worker = PeriodicWorker(
            name=f"{self._thread_prefix}-{name}",
            interval=interval,
            is_daemon=is_daemon,
            target=target,
            args=args,
        )
        with self._worker_lock:
            self._workers.append(worker)
        return worker

    def start_worker(self, worker: WorkerThread) -> None:
        """Start a worker thread"""
        worker.start()

    def stop_worker(self, worker: WorkerThread, timeout: float = 5.0) -> None:
        """Stop a worker thread"""
        worker.stop(timeout=timeout)
        with self._worker_lock:
            if worker in self._workers:
                self._workers.remove(worker)

    def start_all(self) -> None:
        """Start all registered workers"""
        self._running = True
        with self._worker_lock:
            for worker in self._workers:
                if not worker.is_running():
                    worker.start()

    def stop_all(self, timeout: float = 10.0) -> None:
        """Stop all workers"""
        self._running = False
        with self._worker_lock:
            for worker in self._workers:
                if worker.is_running():
                    worker.stop(timeout=timeout)
            self._workers.clear()

    def get_worker_info(self, name: str) -> Optional[ThreadInfo]:
        """Get information about a specific worker"""
        with self._worker_lock:
            for worker in self._workers:
                if worker.name == name or worker.name.endswith(f"-{name}"):
                    return worker.get_info()
        return None

    def get_all_worker_info(self) -> List[ThreadInfo]:
        """Get information about all workers"""
        with self._worker_lock:
            return [w.get_info() for w in self._workers]

    def shutdown(self, timeout: float = 10.0) -> None:
        """Shutdown thread pool and all workers"""
        self.stop_all(timeout=timeout)
        self._executor.shutdown(wait=True, cancel_futures=True)

    def is_running(self) -> bool:
        """Check if any workers are running"""
        return self._running


class BackgroundTaskManager:
    """
    High-level task manager for background operations.
    Provides task queue and progress tracking.
    """

    def __init__(self, max_workers: int = 4) -> None:
        """Initialize task manager"""
        self._pool = ThreadPoolManager(max_workers=max_workers)
        self._tasks: Dict[str, Task] = {}
        self._task_lock = Lock()
        self._progress_callbacks: Dict[str, Callable[[Dict[str, Any]], None]] = {}

    def submit(
        self,
        task_id: str,
        func: Callable[..., Any],
        *args: Any,
        on_progress: Optional[Callable[[Dict[str, Any]], None]] = None,
        **kwargs: Any,
    ) -> str:
        """Submit a background task"""
        task = Task(
            task_id=task_id,
            name=task_id,
            func=func,
            args=args,
            kwargs=kwargs,
        )
        with self._task_lock:
            self._tasks[task_id] = task
        if on_progress is not None:
            self._progress_callbacks[task_id] = on_progress

        future = self._pool.submit_task(func, *args, **kwargs)
        self._tasks[task_id].state = ThreadState.RUNNING
        return task_id

    def get_result(self, task_id: str, timeout: Optional[float] = None) -> Any:
        """Get task result"""
        with self._task_lock:
            task = self._tasks.get(task_id)
        if task is None:
            raise ValueError(f"Task {task_id} not found")
        if task.func is None:
            return None
        future = self._pool.submit_task(task.func, *task.args, **task.kwargs)
        return future.result(timeout=timeout)

    def get_status(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Get task status"""
        with self._task_lock:
            task = self._tasks.get(task_id)
        if task is None:
            return None
        return {
            "id": task.task_id,
            "name": task.name,
            "state": task.state.value,
            "error": task.error,
            "created_at": task.created_at.isoformat(),
        }

    def cancel(self, task_id: str) -> bool:
        """Cancel a pending task"""
        with self._task_lock:
            task = self._tasks.get(task_id)
        if task is not None and task.state in (
            ThreadState.CREATED,
            ThreadState.STARTING,
        ):
            self._tasks.pop(task_id, None)
            return True
        return False

    def wait_for_completion(
        self, task_ids: Optional[List[str]] = None, timeout: Optional[float] = None
    ) -> bool:
        """Wait for tasks to complete"""
        tasks_to_wait = task_ids or list(self._tasks.keys())
        start_time = time.time()
        for task_id in tasks_to_wait:
            remaining = timeout - (time.time() - start_time) if timeout else None
            if remaining is not None and remaining <= 0:
                return False
            try:
                self.get_result(task_id, timeout=remaining)
            except TimeoutError:
                return False
        return True

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        """Get status of all tasks"""
        with self._task_lock:
            return [
                {
                    "id": task.task_id,
                    "name": task.name,
                    "state": task.state.value,
                    "error": task.error,
                }
                for task in self._tasks.values()
            ]

    def shutdown(self) -> None:
        """Shutdown task manager"""
        self._pool.shutdown()
        self._tasks.clear()
        self._progress_callbacks.clear()


def create_worker_thread(
    name: str,
    target: Callable[..., Any],
    args: tuple = (),
    is_daemon: bool = True,
) -> WorkerThread:
    """Create a worker thread"""
    return WorkerThread(
        name=name,
        is_daemon=is_daemon,
        target=target,
        args=args,
    )


def create_periodic_worker(
    name: str,
    interval: float,
    target: Callable[..., Any],
    args: tuple = (),
    is_daemon: bool = True,
) -> PeriodicWorker:
    """Create a periodic worker thread"""
    return PeriodicWorker(
        name=name,
        interval=interval,
        is_daemon=is_daemon,
        target=target,
        args=args,
    )
