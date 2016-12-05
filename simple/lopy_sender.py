import socket
import time

from network import LoRa
i = 0
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
print("Ready to send data...")

while (True):
    msg = bytes([0xff, 0xff, 0x00, 0x00, 0x07,  i, 0xab])
    i+=1
    if (i == 0xff):
        i=0
    lora_sock.send(msg)
    print("Sent!")
    time.sleep(5)

