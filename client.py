#!/usr/local/bin/python3
import socket
import time

from UDP_Socket import *



def main():
    client = UDP_Socket()
    client.isClient();


    message = b"your very important message"
    while True:
        client.sendto(message)
        print("message sent!")
        time.sleep(1)


if __name__ == "__main__":
    main()


