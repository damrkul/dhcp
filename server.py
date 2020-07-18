#!/usr/bin/python3
import socket
from UDP_Socket import *
from helpers import *
from  DHCP_Packet import *
from  DHCP_Options import *
import DHCP_Messages


def main():
    server = UDP_Socket("Server")
    print("PORT: " + str(server.port ))
    print("SEND PORT: " + str(server.send_port))
    while True:

        data, addr = server.recvfrom()
#        print ( addr )
        packet = DHCP_Packet()
        packet.decode(data)
      #  packet.to_string()

        print("")
        print("")
        print("================")
        ## Which Reply to Make

        ## Since we will always be creating a REply, I will be taking
        # message_type and adding +1 to call the next reply
        # Example: if packet.dhcp_message_type = 1 (DHCPDiscover)
        # I'll be actually calling dhcp_methods.get(2) because that is the Offer Packet
        message_type = hexbinary_to_int(packet.dhcp_message_type)
        if message_type == DHCP_DISCOVER:
            myFunc = DHCP_Messages.dhcp_methods.get(DHCP_OFFER)
            print("Recieved from " + str(addr) + ": " + op_name[message_type] + " | Sending Back: " + op_name[DHCP_OFFER])
        elif message_type == DHCP_REQUEST:
            myFunc = DHCP_Messages.dhcp_methods.get(DHCP_ACK)
            print("Recieved from " + str(addr) +": "+  op_name[message_type] + " | Sending Back: " + op_name[DHCP_ACK])

#        myFunc = DHCP_Messages.dhcp_methods.get(hexbinary_to_int(packet.dhcp_message_type) + 1 )
        
        packetReply = myFunc(packet)
        server.sendto(packetReply)
        print("================")
        if message_type == DHCP_REQUEST:
            print("DHCPACK Packet Info") 
            ack_packet = DHCP_Packet()
            ack_packet.decode(packetReply)  
            ack_packet.to_string()



if __name__ == "__main__":
    main()
