#!/usr/bin/python
# -*- coding: UTF-8 -*-

from zlib import crc32
import os
import sys

def getCrc32(filename):
	with open(filename, 'rb') as f:
		return crc32(f.read())&0xffffffff

def putCrc32(file_path, msg):
    f=open(file_path,"w")
    f.write(msg)
    f.close

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print ("Usage: python create_deploy_pic_crc.py <input_file>")
		exit(-1)

	if (False == os.path.exists(sys.argv[1])):
		print ("Error: input file '%s' not exist" % sys.argv[1])
		exit(-1)

	input_file = sys.argv[1]

	checksum=getCrc32(input_file)
	
	output_file = input_file.replace('.jpg','_crc32.dat')
	print (output_file)

	putCrc32(output_file, hex(checksum))

	print ("Crc:",(hex(checksum)))

	exit(0)

