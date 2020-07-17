#!/usr/local/bin/python3
import socket

class UDP_Socket:
    def __init__(self):
#        self.port = 32067
        self.port = 67
        try:
            self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
        except:
            print("Cannot create UDP Socket")

        try:
            self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        except:
            print("Cannot set Socket Reuse port")
        try:
            self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except:
            print("Cannot set socket for Broadcast")
        try:
            self.sockfd.bind(("", self.port))
        except:
            printf("Cannot Bind Socket to Port" + self.port )

    def recvfrom(self):
        '''data, addr = server.recvfrom() '''
        return self.sockfd.recvfrom(1024)

    def sendto(self,message):
        self.sockfd.sendto(message, ('255.255.255.255', self.port))


    """ # Set a timeout so the socket does not block  indefinitely when trying to receive data."""
    def isClient(self):
        self.sockfd.settimeout(0.2)


