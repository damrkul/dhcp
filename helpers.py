import socket
import binascii
def int_to_hexbinary(number):
    number = str(number)
    if len(number) % 2 == 1:
        number =number.zfill(len(number) + 1)
    return binascii.unhexlify(number)

def hexbinary_to_int(hexbin):
    return int(binascii.hexlify(hexbin))

""" Convert 0024e865a023 to 00:24:e8:65:a0:23 """
def mac_readable(binstring):
    mac = binstring.decode('ascii')
    return  ':'.join([mac[i:i+2] for i,j in enumerate(mac) if not (i%2)])
def strip_colon(mac):
    return mac.replace(":","")


def mac_hextobin(mac):
    return binascii.unhexlify(mac)

def mac_bintohex(mac):
    return binascii.hexlify(mac)
