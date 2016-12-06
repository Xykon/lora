#!/usr/bin/env python3

import struct
from loranode.rpyutils import printd, Level, Color, clr, set_debug_level
from threading import Thread, Lock
from loranode import RN2483Controller
from time import sleep

class ReceiverThread(Thread):
    def __init__(self, mutex):
        Thread.__init__(self)
        self.setDaemon(True)
        self.lc = RN2483Controller("/dev/ttyACM0")
        self.lc.set_sf("7")
        self.lc.set_pwr("15")
        self.lc.get_bt()
        self.lc.set_bt("none")
        #self.lc.set_freq("868000000")
        print("LoRa frequency: ",self.lc.get_freq())
        self.mutex = mutex
        self.counter = 0

    def run(self):
        while True:
            r = self.lc.recv_p2p()

            self.mutex.acquire() # Do not let prints occur simultaneously
            printd(clr(Color.BLUE, "RECV[" + str(self.counter) + "]: " + r), Level.INFO)
            self.counter += 1
            self.mutex.release()

# LoRaController peer-to-peer test, assuming receiver device on /dev/ttyACM0

if __name__ == "__main__":
    set_debug_level(Level.DEBUG)

    m = Lock()

    r = ReceiverThread(m)
    r.start()

    r.join()
