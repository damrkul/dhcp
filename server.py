#!/usr/local/bin/python3
import socket
from UDP_Socket import *



def main():
    server = UDP_Socket()
    while True:
        # Thanks @seym45 for a fix
        data, addr = server.recvfrom()
        print ( addr )
        print("received message: %s"%data)



if __name__ == "__main__":
    main()
