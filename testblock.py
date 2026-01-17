#! /usr/bin/env python3

import re
import urllib.request
from typing import Any

debug = False


class bitcoinapi:

    def _debug(self, message):
        if debug:
            print(message)

    def _grabapi(self, apipaths):
        # This will attempt to grab the information using blockchain first, then blockexplorer.
        sources = ["http://blockchain.info", "http://blockexplorer.com"]
        urls = ["".join(t) for t in zip(sources, apipaths)]
        # print(urls)
        for url in urls:
            try:
                self._debug("Getting: " + url)
                user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
                headers = {"User-Agent": user_agent}
                bitOpen = urllib.request.Request(url, None, headers)
                data = urllib.request.urlopen(bitOpen).read().decode("utf-8")
                # data = urlopen(url, timeout=5).read()
                if data == "":
                    self._debug("Got a blank response")
                    continue
                self._debug("Got: " + data)
                return data
            except Exception as e:
                self._debug(e)
                continue
        return None

    def get_interval(self):
        # Average time between blocks in seconds
        currentint = self._grabapi(["/q/interval"] * 2)
        if currentint is None or currentint == "":
            self._debug("Opps, there was an error, try later")
            return
        return float(currentint)

    def get_currentblock(self):
        # Current block height in the longest chain
        currentblock = self._grabapi(["/q/getblockcount"] * 2)
        if currentblock is None or currentblock == "":
            self._debug("Opps, there was an error, try later")
            return
        return float(currentblock)

    def get_hashrate(self):
        # Estimated network hash rate in gigahash
        hashrate = self._grabapi(["/q/hashrate"] * 2)
        if hashrate is None or hashrate == "":
            self._debug("Opps, there was an error, try later")
            return
        return float(hashrate)

    def get_nextdifficulty(self):
        # Get the next difficulty (Only available from blockexplorer)
        nextdiff = self._grabapi(["/q/estimate"] * 2)
        if nextdiff is None or nextdiff == "":
            self._debug("Opps, there was an error, try later")
            return
        return float(nextdiff)

    def get_difficulty(self):
        # Current difficulty target as a decimal number
        currentdiff = self._grabapi(["/q/getdifficulty"] * 2)
        if currentdiff is None or currentdiff == "":
            self._debug("Opps, there was an error, try later")
            return
        return float(currentdiff)

    def get_nextretarget(self):
        # Block height of the next difficulty retarget
        nextretarget = self._grabapi(["/q/nextretarget"] * 2)
        if nextretarget is None or nextretarget == "":
            self._debug("Opps, there was an error, try later")
            return
        return float(nextretarget)

    def stat_hash(self):
        # Hash Stats
        currentint = self.get_interval()
        currentblock = self.get_currentblock()
        hashrate = self.get_hashrate()

        if currentint is None or currentblock is None or hashrate is None:
            return "There was an error, please try again later"

        m, s = divmod(currentint, 60)
        abouttime = "%02d Minutes %02d Seconds" % (m, s)
        data = "Estimated interval between blocks: %s | Current Block: %d | Global Hashrate: %.2f GH/s " % (
            abouttime,
            currentblock,
            hashrate,
        )
        return data

    def stat_diff(self):
        # Difficulty Stats
        nextretarget = self.get_nextretarget()
        currentblock = self.get_currentblock()
        nextdiff = self.get_nextdifficulty()
        currentdiff = self.get_difficulty()
        currentint = self.get_interval()

        if nextretarget is None or currentblock is None or nextdiff is None or currentdiff is None or currentint is None:
            return "There was an error, please try again later"

        nextin = nextretarget - currentblock
        diffchange = (nextdiff - currentdiff) / currentdiff * 100
        timetochange = nextin * currentint
        m, s = divmod(timetochange, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        abouttime = "%d Days %d Hours %02d Minutes %02d Seconds" % (d, h, m, s)
        data = "Cur Dif: %.2f | Est Next: %.2f (%.2f%%) | Next Diff change in: %d Blocks (~%s)" % (
            currentdiff,
            nextdiff,
            diffchange,
            nextin,
            abouttime,
        )
        return data

    def gettxid(self, txid):
        # For now we will just use blockchain.info since block explorers is a bit different. Besides, soon I will be downloading the blockchain
        tx = urllib.request.urlopen("http://blockchain.info/rawtx/" + txid)
        tx = tx.read().decode("utf-8")
        print(tx)
        if tx is None or tx == "":
            self._debug("Opps, there was an error, try later")
            return
        return tx

    def stat_estimate(self, hashrate, quote=0):
        currentdiff = self.get_difficulty()

        if currentdiff is None:
            return "There was an error, please try again later"

        estimate = 24 / (currentdiff * 2**32 / (hashrate * 10**6) / 60 / 60) * 25
        if quote == 0:
            data = "At %d MH/s, you should earn on avg ~%f BTC/day or %f BTC/hr." % (
                hashrate,
                estimate,
                (estimate / 24),
            )
        else:
            data = "At %d MH/s, you should earn on avg ~%f BTC/day ($%f USD) or %f BTC/hr." % (
                hashrate,
                estimate,
                (estimate * quote),
                (estimate / 24),
            )
        return data


if __name__ == "__main__":
    btcapi = bitcoinapi()
    # Unit tests
    ch = ""
    t = 0
    r = 0
    m: Any
    try:
        import msvcrt as m
    except ImportError:
        m = None
    import calendar
    import datetime
    import time

    print((calendar.isleap(2014)))
    try:
        timex = urllib.request.urlopen("http://just-the-time.appspot.com/").read().decode("utf-8")
        matchObj = re.match(r"(.*)-(.*?)-(.*?) (.*?):(.*?):(.*?) UTC", timex, re.M | re.I)
        if matchObj:
            HaloTimeHour = datetime.datetime(
                int(matchObj.group(1)),
                int(matchObj.group(2)),
                int(matchObj.group(3)),
                int(matchObj.group(4)),
                int(matchObj.group(5)),
                int(matchObj.group(6)),
            )
            print(HaloTimeHour)
            print(timex)
        else:
            print("Time format not matched: " + timex)
    except Exception as e:
        print(("Time fetch failed:", e))

    print((datetime.date.today))
    print((datetime.datetime))
    try:
        print((btcapi.gettxid("59e0a90ebe8fa15a9ee828fa67d417d391338b01d87bdfc7d0482b3f74af9932")))
    except Exception as e:
        print(("Tx fetch failed:", e))

    if m:
        m.getch()
    else:
        # Compatibility for Linux
        try:
            eval(input("Press Enter to continue."))
        except Exception:
            pass

    print(("block:", btcapi.get_currentblock(), "  interval:", r))
    while ch == "":
        time.sleep(60)
        t += 1
        if t == 10:
            r += 1
            t = 0
            print(("block:", btcapi.get_currentblock(), "  interval:", r))
    print((btcapi.get_currentblock()))
    print((btcapi.get_nextretarget()))
    print((btcapi.stat_hash()))
    print((btcapi.stat_diff()))
    print((btcapi.stat_estimate(100)))
    print((btcapi.stat_estimate(100, 118.4)))
