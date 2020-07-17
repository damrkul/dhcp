# This is DHCP Packet

# http://www.tcpipguide.com/free/t_DHCPMessageFormat.htm
# http://www.tcpipguide.com/free/t_BOOTPMessageFormat.htm
import helpers
import struct
from socket import inet_aton,inet_ntoa,ntohs, ntohl,htons, htonl
#from network_utils import mac_hextostr,mac_strtohex
import binascii
from DHCP_Options import dhcp_options
"""mac_hextostr

def hextobin(macaddr)
    return binascii.unhexlify(macaddr.replace(b':', b''))
def bintohex(macaddr)
    return binascii.hexlify(macaddr))
"""

class DHCP_Packet:
    def __init__(self):
        # Size = 1
        self.op = 1
        self.htype = 1
        self.hlen = 6
        self.hops = 0
        self.xid = None
        self.secs =  60
        self.flags = {  "B" : 1 , "Reserved": 0 }
        self.ciaddr = '0.0.0.0'
        self.yiaddr = '0.0.0.0'
        self.siaddr = '0.0.0.0'
        self.giaddr = '0.0.0.0'
        self.chaddr = 'mac'
        self.sname = "mywebsite.com"
        self.file = ""
        self.vend = ""
        self.options = {}


    def encode(self):
        '''   The options field is now variable length, with the minimum extended
   to 312 octets.  This brings the minimum size of a DHCP message up to
   576 octets, the minimum IP datagram size a host must be prepared to
   accept [3].  DHCP clients may negotiate the use of larger DHCP
   messages through the 'Maximum DHCP message size' option.  The options
   field may be further extended into the 'file' and 'sname' field'''

    #   ntohs(), ntohl() -- convert 16, 32 bit int from network to host byte order
  #  htons(), htonl() -- convert 16, 32 bit int from host to network byte order
    #inet_aton() -- convert IP addr string (123.45.67.89) to 32-bit packed format
  #  inet_ntoa() -- convert 32-bit packed format IP to string (123.45.67.89)


        message = bytearray(236)
        op              = helpers.int_to_hexbinary(1)
        htype           = helpers.int_to_hexbinary(1)
        hlen            = helpers.int_to_hexbinary(6)
        hops            = helpers.int_to_hexbinary(4)
        message[0:4]    = op + htype +hlen + hops
        message[4:8]    = self.trans_id =  struct.pack('>I', 234324)
        message[8:10]   = self.secs = struct.pack('>H', 0)
#        message[10:12]  = self.flags = struct.pack('>H', bin('1000000000000000'))
        message[10:12]  = self.flags =  b'\x80\x00' ## Set Broadcast flag
        message[12:16]  = self.ciaddr = inet_aton('10.10.0.1')
        message[16:20]  = self.yiaddr = inet_aton('0.0.0.0')
        message[20:24]  = self.siaddr = inet_aton('0.0.0.0')
        message[24:28]  = self.giaddr = inet_aton('0.0.0.0')
        message[28:34]  = self.chaddr = helpers.mac_hextobin(helpers.strip_colon("f0:18:98:8f:2c:33"))
        message += inet_aton('99.130.83.99') # Magic Number

        message+=bytes([53]) + bytes([1]) + bytes([1])
        message+=bytes([55]) + bytes([4]) + bytes([1]) + bytes([3]) + bytes([6]) + bytes([28])

        message += b'\xFF'
        return message

    def decode(self,message):
        ''' This is literally the Inverse of encode packet.  Its just useful to
        to decode it back into the DHCP_Packet object for Troubleshooting.'''
        self.op         = message[0]
        self.htype      = message[1]
        self.hlen       = message[2]
        self.hops       = message[3]
        self.trans_id   = struct.unpack('>I', message[4:8])[0]
        self.secs       = struct.unpack('>H', message[8:10])[0]
        self.flags      = struct.unpack('>H', message[10:12] )[0]
        self.ciaddr     = inet_ntoa(message[12:16])
        self.yiaddr     = inet_ntoa(message[16:20])
        self.siaddr     = inet_ntoa(message[20:24])
        self.giaddr     = inet_ntoa(message[24:28])
        self.chaddr     = helpers.mac_bintohex(message[28:34])

        optionIndex = self.findMagicCookie(message) + 4

        print("magic cookie found at index: " + str( optionIndex) )
        self.options = self.parseOptions(message,optionIndex)
        self.dhcp_message_type = self.options[53]['data']



    def findMagicCookie(self, message):
        index = 34;
        magicCookie = inet_aton('99.130.83.99')
        while index < len(message):
            if message[index:index+4] == magicCookie:
                return index
            index +=1

        return -1

    def parseOptions(self,message, index):
        """
        Starting and the first Index AFTER Magic Cookie;
        [code][length][value]

        Example:
        [53][1][value]]
        [53][2][value][value]


        TODO: Make DICT data structure to hold various Options + Lengths
        based off RFC """
        options =  {}

        while index < len(message):
            if message[index] == 255: # END OPTION
                options[255] = { 'data': b'\xFF' ,
                                   'tag': 255 ,
                                   'length': 0,
                                   'name': dhcp_options[255]['name'] }
                return options


            optionCode = message[index]
            if  optionCode == 0:
                index+=1
                continue

            """ This is parsing out the Code+length+data """
            optionLength = message[index+1]
            optionData = bytearray(optionLength)
            optionData[0:optionLength] =  message[index+2:index+2+optionLength]
            options[optionCode] = { 'data': optionData ,
                                   'tag': optionCode ,
                                   'length': optionLength,
                                   'name': dhcp_options[optionCode]['name'] }
            index+=2+optionLength

        return options





    def to_string(self):
        print("======= DHCP Packet Contents =====")
        print("self.op       = "  +  str(self.op) )
        print("self.hytpe    = "  +  str(self.htype) )
        print("self.hlen     = "  +  str(self.hlen) )
        print("self.hops     = "  +  str(self.hops) )
        print("self.trans_id = "  +  str(self.trans_id) )
        print("self.secs     = "  +  str(self.secs) )
        print("self.flags    = "  +  str(self.flags) )
        print("self.ciaddr   = "  +  str(self.ciaddr) )
        print("self.yiaddr   = "  +  str(self.yiaddr) )
        print("self.siaddr   = "  +  str(self.siaddr) )
        print("self.giaddr   = "  +  str(self.giaddr) )
        print("self.chaddr   = "  +  str(self.chaddr) )
        print("======= End Contents =====")

        print("==== DHCP OPTIONS Found ===")
        for key in self.options.keys():
            print("tag: " + str(key) + " | name: " + self.options[key]['name']
                  + " | length: " + str(self.options[key]['length'])
                  + " | data: "  + str(self.options[key]['data']))
        if 55 in self.options:
            print("==== DHCP Requesting Options Found ===")
            for i in self.options[55]['data']:
                print( "Requesting | Code: " +  str(i)  + " name: "+ dhcp_options[i]['name'] )

