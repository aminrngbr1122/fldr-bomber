#!usr/bin/env python3
# Date: 1-18-18, Jan ~ 18th 2018 | Synchronocy
# Project: Folder Bomber
# IDLE Python 3.6 64-bit

import uuid 
import os
import sys

def folder(amt):
	for count in range(amt): # Using our value in main() to loop through the makedirs.
		os.makedirs(str(uuid.uuid4()))
		print(count)

def main():
	amt = input("Amount of folders: ")
	folder(int(amt)) # just reassuring that its an integer not an ascii character,
    
if __name__ == '__main__':
	main()
	sys.exit()
