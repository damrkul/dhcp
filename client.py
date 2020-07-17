#!/usr/local/bin/python3
import struct
import socket
from  socket import inet_aton
import time
import helpers
from UDP_Socket import *
from DHCP_Packet import *
import binascii





def main():
    client = UDP_Socket()
    client.isClient()
    packet = DHCP_Packet()
    print(packet.encode())
    while True:
        client.sendto(packet.encode())
        print("message sent!")
        time.sleep(1)


if __name__ == "__main__":
    main()


