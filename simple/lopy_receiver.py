import socket
import time
import binascii
from network import LoRa
print("Initializing LoRa module...")

lora = LoRa(mode=LoRa.LORA,
            frequency=868100000,
            tx_power=14,
            bandwidth=LoRa.BW_125KHZ,
            sf=7,
            coding_rate=LoRa.CODING_4_5,
            power_mode=LoRa.ALWAYS_ON)
            
lora_sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
lora_sock.setblocking(False)

print("Waiting for data...")
while (True):
    rbuf=lora_sock.recv(255)
    if (len(rbuf) > 0):
        print(binascii.hexlify(rbuf, '  '))
    time.sleep_ms(100)

