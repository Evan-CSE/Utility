# Bismilla-hir Rahma-nir Rahi-m

import socket

print("Welcome user");
while True:
	site = input("Enter url ");


	ip = socket.gethostbyname(site);

	print("Obtaingin Ip address of " + site);

	print(ip);


print("Script written by Evan")
