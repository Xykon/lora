#!/usr/bin/env python3

import struct
from loranode.rpyutils import printd, Level, Color, clr, set_debug_level
from threading import Thread, Lock
from loranode import RN2483Controller
from time import sleep

class TransmitterThread(Thread):
    def __init__(self, mutex):
        Thread.__init__(self)
        self.setDaemon(True)
        self.lc = RN2483Controller("/dev/ttyACM0")
        self.lc.set_sf("7")
        self.lc.set_pwr("15")
        self.lc.get_bt()
#        self.lc.set_bt("none")
#        self.lc.set_freq("868000000")
        print("LoRa frequency: ",self.lc.get_freq())
        self.mutex = mutex
        self.counter = 4278190080
#        self.counter = 0

    def run(self):
        while True:
            data = struct.pack(">I", self.counter).hex()
            self.counter += 1

            self.mutex.acquire()
            printd(clr(Color.GREEN, "SEND: " + data), Level.INFO)
            self.mutex.release()

            r = self.lc.send_p2p(data)
            sleep(3)

# LoRaController peer-to-peer test, assuming sender device at /dev/ttyACM0

if __name__ == "__main__":
    set_debug_level(Level.DEBUG)

    m = Lock()

    t = TransmitterThread(m)
    t.start()

    t.join()
