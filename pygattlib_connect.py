from __future__ import print_function

import sys
from gattlib import GATTRequester


class JustConnect(object):
    def __init__(self, address):
        self.requester = GATTRequester(address, False)
        self.connect()

    def connect(self):
        print("Connecting...", end=' ')
        sys.stdout.flush()

        self.requester.connect(True)
        print("OK!")

if __name__ == '__main__':
    JustConnect("CA:34:A7:E4:DF:50")
    print("Done.")
