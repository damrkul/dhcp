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
    client = UDP_Socket("Client")
    client.isClient()
    packet = DHCP_Packet()
    print(packet.encode())
#    while True:
    client.sendto(packet.encode())
    packet.to_string()
    time.sleep(1)

    data, addr = client.recvfrom()
    print ( addr )
    print ("RECIEVING...........")
    packet = DHCP_Packet()
    packet.decode(data)
    packet.to_string()





if __name__ == "__main__":
    main()


