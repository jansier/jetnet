import socket
import sys

if True:
    # Get "IP address of Server" and also the "port number" from
    ip = '192.168.1.73'
    port = 8765
else:
    print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
    exit(1)

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM | SOCK_DGRAM)
# Bind the socket to the port
server_address = (ip, port)
sock.bind(server_address)

while True:
    print("####### Server is listening #######")
    data, address = sock.recvfrom(4096)
    print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
    send_data = input("Type some text to send => ")
    sock.sendto(send_data.encode('utf-8'), address)
    print("\n\n 1. Server sent : ", send_data,"\n\n")