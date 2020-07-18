import DHCP_Config
from socket import inet_aton
import struct
import DHCP_Packet
DHCP_DISCOVER   = 1
DHCP_OFFER      = 2
DHCP_REQUEST    = 3
DHCP_DECLINE    = 4
DHCP_ACK        = 5
DHCP_NAK        = 6
DHCP_RELEASE    = 7


def dhcp_method_discover():
    print("This is discover Method")

def dhcp_method_offer(packet):
    # Message Type == Request
    packet.op = 2
    packet.yiaddr = DHCP_Config.ip_pool[0]
    packet.giaddr = DHCP_Config.gateway
    options = bytes([53]) +  bytes([1]) + bytes([2])

    # Subnet Mask
    options += bytes([1]) +  bytes([4]) + inet_aton(DHCP_Config.subnetmask)
    options += bytes([3])  + bytes([4]) + inet_aton(DHCP_Config.gateway)
    options += bytes([28])  + bytes([4]) + inet_aton(DHCP_Config.broadcast)
    options += bytes([51])  +  bytes([4]) + struct.pack('>I', 600)

    message = packet.prepare_packet()

    message += options +  b'\xFF'

    return  message


def dhcp_method_request(packet):
    print("This is REQUEST Method")
def dhcp_method_decline(packet):
    print("This is decline Method")

def dhcp_method_ack(packet):
    # Message Type == Request
    packet.yiaddr = DHCP_Config.ip_pool[0]
    packet.giaddr = DHCP_Config.gateway
    options = bytes([53]) +  bytes([1]) + bytes([5])

    # Subnet Mask
    options += bytes([1]) +  bytes([4]) + inet_aton(DHCP_Config.subnetmask)
    options += bytes([3]) +  bytes([4]) + inet_aton(DHCP_Config.gateway)
    options += bytes([28]) +  bytes([4]) + inet_aton(DHCP_Config.broadcast)
    options += bytes([51])  + bytes([4]) + struct.pack('>I', 600)

    message = packet.prepare_packet()

    message += options +  b'\xFF'

    return message
def dhcp_method_nak(packet):
    print("This is nak Method")

def dhcp_method_release(packet):
    print("This is release Method")




dhcp_methods =  {
    1: dhcp_method_discover,
    2: dhcp_method_offer,
    3: dhcp_method_request,
    4: dhcp_method_decline,
    5: dhcp_method_ack,
    6: dhcp_method_ack,
}

