#!/usr/local/bin/python3
import socket
from UDP_Socket import *
from helpers import *
from  DHCP_Packet import *
from  DHCP_Options import *
import DHCP_Messages

def main():
    server = UDP_Socket()
    while True:
        # Thanks @seym45 for a fix
        data, addr = server.recvfrom()
        print ( addr )
        packet = DHCP_Packet()
        packet.decode(data)
        packet.to_string()

        print("")
        print("")
        ## Which Reply to Make

        ## Since we will always be creating a REply, I will be taking
        # message_type and adding +1 to call the next reply
        # Example: if packet.dhcp_message_type = 1 (DHCPDiscover)
        # I'll be actually calling dhcp_methods.get(2) because that is the Offer Packet
        print(hexbinary_to_int(packet.dhcp_message_type))
        myFunc = dhcp_methods.get(hexbinary_to_int(packet.dhcp_message_type) + 1 )
        myFunc()

if __name__ == "__main__":
    main()
