#! /usr/bin/env python3

import argparse
import logging
import time
import urllib.request
from typing import List, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


class bitcoinapi:

    def _grabapi(self, apipaths: List[str]) -> Optional[str]:
        # Using blockchain.info only as blockexplorer is deprecated/unreliable
        sources = ["https://blockchain.info"]
        urls = ["".join(t) for t in zip(sources, apipaths)]

        for url in urls:
            try:
                logger.debug(f"Getting: {url}")
                user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
                headers = {"User-Agent": user_agent}
                bitOpen = urllib.request.Request(url, None, headers)
                # Timeout set to 10s
                data = urllib.request.urlopen(bitOpen, timeout=10).read().decode("utf-8")

                if data == "":
                    logger.debug("Got a blank response")
                    continue
                logger.debug(f"Got: {data}")
                return data
            except Exception as e:
                logger.error(f"Error fetching {url}: {e}")
                continue
        return None

    def get_interval(self) -> Optional[float]:
        # Average time between blocks in seconds (Approximate or fetched)
        # Blockchain.info doesn't have a direct "interval" endpoint in q/api strictly documented as stable,
        # but we preserve legacy endpoint or defaulting if missing.
        # Actually /q/interval exists on blockchain.info.
        currentint = self._grabapi(["/q/interval"])
        if currentint is None or currentint == "":
            logger.error("Failed to get interval")
            return None
        try:
            return float(currentint)
        except ValueError:
            return None

    def get_currentblock(self) -> Optional[int]:
        # Current block height in the longest chain
        currentblock = self._grabapi(["/q/getblockcount"])
        if currentblock is None or currentblock == "":
            logger.error("Failed to get block count")
            return None
        try:
            return int(float(currentblock))
        except ValueError:
            return None

    def get_hashrate(self) -> Optional[float]:
        # Estimated network hash rate in gigahash
        hashrate = self._grabapi(["/q/hashrate"])
        if hashrate is None or hashrate == "":
            logger.error("Failed to get hashrate")
            return None
        try:
            return float(hashrate)
        except ValueError:
            return None

    def get_difficulty(self) -> Optional[float]:
        # Current difficulty target as a decimal number
        currentdiff = self._grabapi(["/q/getdifficulty"])
        if currentdiff is None or currentdiff == "":
            logger.error("Failed to get difficulty")
            return None
        try:
            return float(currentdiff)
        except ValueError:
            return None

    def get_nextretarget(self) -> Optional[int]:
        # Block height of the next difficulty retarget
        # Deterministic calculation: (current_block // 2016 + 1) * 2016
        current_block = self.get_currentblock()
        if current_block is None:
            logger.error("Failed to get current block for retarget calculation")
            return None
        return (current_block // 2016 + 1) * 2016

    def get_bcperblock(self) -> Optional[float]:
        # Block reward
        reward = self._grabapi(["/q/bcperblock"])
        if reward is None or reward == "":
            logger.error("Failed to get block reward")
            return None
        try:
            return float(reward)
        except ValueError:
            return None

    def stat_hash(self) -> str:
        # Hash Stats
        currentint = self.get_interval()
        currentblock = self.get_currentblock()
        hashrate = self.get_hashrate()

        if currentint is None or currentblock is None or hashrate is None:
            return "There was an error, please try again later"

        # Fix: divmod works on floats in Py3, returning float. Cast to int for %d formatting.
        m, s = divmod(int(currentint), 60)
        abouttime = "%02d Minutes %02d Seconds" % (m, s)
        data = "Estimated interval between blocks: %s | Current Block: %d | Global Hashrate: %.2f GH/s " % (
            abouttime,
            currentblock,
            hashrate,
        )
        return data

    def stat_diff(self) -> str:
        # Difficulty Stats
        nextretarget = self.get_nextretarget()
        currentblock = self.get_currentblock()
        currentdiff = self.get_difficulty()
        currentint = self.get_interval()

        if nextretarget is None or currentblock is None or currentdiff is None or currentint is None:
            return "There was an error, please try again later"

        nextin = nextretarget - currentblock
        # We omitted get_nextdifficulty because /q/estimate is unreliable.
        # We will omit "Est Next" and "Diff change" percent from the output if we don't have it.
        # Or we could calculate it if we had reliable time data, but simpler is safer.

        timetochange = nextin * currentint
        # Fix: Cast to int for formatting
        m, s = divmod(int(timetochange), 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        abouttime = "%d Days %d Hours %02d Minutes %02d Seconds" % (d, h, m, s)

        data = "Cur Dif: %.2f | Next Diff change in: %d Blocks (~%s)" % (
            currentdiff,
            nextin,
            abouttime,
        )
        return data

    def gettxid(self, txid: str) -> Optional[str]:
        # Use HTTPS
        url = "https://blockchain.info/rawtx/" + txid
        try:
            response = urllib.request.urlopen(url, timeout=10)
            tx = response.read().decode("utf-8")
            logger.debug(f"Transaction data for {txid} fetched.")
            if tx == "":
                logger.error("Got blank response for txid")
                return None
            return tx
        except Exception as e:
            logger.error(f"Error fetching txid {txid}: {e}")
            return None

    def stat_estimate(self, hashrate: float, quote: float = 0.0) -> str:
        currentdiff = self.get_difficulty()
        reward = self.get_bcperblock()

        if currentdiff is None or reward is None:
            return "There was an error (missing difficulty or reward), please try again later"

        # Standard Mining Formula:
        # Earnings (BTC/day) = (Hashrate (MH/s) * 1e6 * Reward * 86400) / (Difficulty * 2^32)
        # Note: input hashrate is usually MH/s in valid mining calcs or script usage.
        # Reference Code used: 24 / (currentdiff * 2**32 / (hashrate * 10**6) / 60 / 60) * 25
        # The input hashrate seems to be in MH/s based on the string "At %d MH/s".

        # New Formula:
        # difficulty * 2^32 = hashes per block
        # hashrate * 10^6 = hashes per second
        # (diff * 2^32) / (hashrate * 10^6) = seconds per block for this user
        # blocks per day = 86400 / seconds per block
        # BTC per day = blocks per day * reward

        hashes_per_block = currentdiff * (2**32)
        hashes_per_sec = hashrate * (10**6)

        if hashes_per_sec == 0:
            return "Hashrate cannot be zero."

        seconds_per_block = hashes_per_block / hashes_per_sec
        blocks_per_day = 86400 / seconds_per_block
        estimate = blocks_per_day * reward

        if quote == 0:
            data = "At %.2f MH/s, you should earn on avg ~%.8f BTC/day or %.8f BTC/hr." % (
                hashrate,
                estimate,
                (estimate / 24),
            )
        else:
            data = "At %.2f MH/s, you should earn on avg ~%.8f BTC/day ($%.2f USD) or %.8f BTC/hr." % (
                hashrate,
                estimate,
                (estimate * quote),
                (estimate / 24),
            )
        return data


def main() -> None:
    parser = argparse.ArgumentParser(description="Bitcoin Network Stats")
    parser.add_argument("--watch", action="store_true", help="Monitor stats continuously (ctrl-c to exit)")
    parser.add_argument("--interval", type=int, default=60, help="Refresh interval in seconds (default: 60)")
    args = parser.parse_args()

    btcapi = bitcoinapi()

    # Initial print
    current_block = btcapi.get_currentblock()
    print("Block:", current_block if current_block else "N/A")
    print(btcapi.stat_hash())
    print(btcapi.stat_diff())

    # Modern hash rate example: 140 TH/s = 140 * 10**6 MH/s
    modern_hashrate = 140 * 10**6
    print(btcapi.stat_estimate(modern_hashrate))
    print(btcapi.stat_estimate(modern_hashrate, 100000.0))  # Example Price

    if args.watch:
        try:
            print(f"\nWatching network status (Interval: {args.interval}s)... Press Ctrl-C to stop.")
            while True:
                time.sleep(args.interval)
                current_block = btcapi.get_currentblock()
                print(f"[{time.strftime('%H:%M:%S')}] Block: {current_block if current_block else 'N/A'}")
        except KeyboardInterrupt:
            print("\nExiting watch mode.")


if __name__ == "__main__":
    main()
