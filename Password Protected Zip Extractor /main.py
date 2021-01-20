#Bismilla-hir Rahma-nir Rahi-m

import zipfile
from art import *

print("[--]By the name of ALLAH [--]");



print(text2art("Script By Evan"));


filename = input("Enter file name ----> ");

ob = zipfile.ZipFile(filename);

password_fl = open("pass.txt","r");

f = False;

for line in password_fl.readlines():
	pw = line.strip('\n')
	pw = bytes(pw,'utf-8');
	if pw=="123456":
		print(pw);
	try:
		f = True;
		ob.extractall(pwd = pw); ## password should be passed in bytes
		print("Password is "+pw+" .....file extracted");
		break;
	except:
		pass
if(f==False):
	print ("Password not found");
