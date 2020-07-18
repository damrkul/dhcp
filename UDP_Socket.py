#!/usr/local/bin/python3
import socket

port = 32067
port = 67
class UDP_Socket:
    def __init__(self, client_or_server):
        if client_or_server == "Server":
            self.port = port
            self.send_port = self.port + 1
        elif client_or_server == "Client":
            self.port = port + 1
            self.send_port = port
        else:
            raise("Please Specify 'Client' or 'Server'")
#        self.port = 67
        self.sockfd = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) # UDP
        self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
        self.sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.sockfd.bind(("", self.port))

        self.sockfd.setsockopt(socket.SOL_SOCKET, 25, str("enp0s8"+'\0').encode('utf-8'))
        if client_or_server == "Client":
            self.sendfd.setsockopt(socket.SOL_SOCKET, 25, str("enp0s8"+'\0').encode('utf-8'))
    def recvfrom(self):
        '''data, addr = server.recvfrom() '''
        return self.sockfd.recvfrom(2024)

    def sendto(self,message):
        self.sockfd.sendto(message, ('<broadcast>', self.send_port))


    """ # Set a timeout so the socket does not block  indefinitely when trying to receive data."""
    def isClient(self):
        self.sockfd.settimeout(0.2)


