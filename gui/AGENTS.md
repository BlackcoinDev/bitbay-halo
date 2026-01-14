# GUI Development Guide

**Updated:** January 2026
**Framework:** PyQt6 | **UI Files:** Qt Designer | **Styles:** CSS/QSS

## OVERVIEW
PyQt6-based GUI with Qt Designer forms and themeable stylesheets.

## STRUCTURE
- **forms/** - 33 Qt Designer .ui files (panels, dialogs, wizards)
- **styles/** - Theme system: base_rc.py, bay_rc.py (auto-generated), CSS files
- **icons/** - Base icons + per-style variants (bitbay/, base/)
- **fonts/** - Roboto font family
- **mainwindow.py** - Main application window (1570+ lines)

## WHERE TO LOOK
- **UI Loading:** `uic.loadUi()` in marketorderdlg.py, mainwindow.py
- **Style switching:** styles/bay.py, styles/btc.py, styles/blk.py
- **Widget references:** mainwindow.py lines 825-832 (le_, l_ pattern)
- **Translation:** YandexTranslate integration (line 31)

## CONVENTIONS
- **Widget naming:** `type_variableName` (le_ = QLineEdit, l_ = QLabel, btn_ = QPushButton)
- **Python vars:** `variableName` (members), `var_name` (temp), `i,j,k` (loop counters)
- **Resource files:** Auto-generated *_rc.py files (DO NOT EDIT)
- **CSS files:** Qt Style Sheets (.qss syntax)

## ANTI-PATTERNS
- **Manual UI code:** Always use Qt Designer, never hand-code UI
- **Direct resource editing:** Modify .qrc files, not *_rc.py files
- **Hardcoded paths:** Use `os.path.abspath(os.path.dirname(__file__))`
- **Mixed naming:** Stick to type_ prefix for all UI widgets