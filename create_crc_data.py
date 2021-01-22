#!/usr/bin/python
# -*- coding: UTF-8 -*-

from zlib import crc32
import os
import sys
import random



def getCrc32(filename):
	with open(filename, 'rb') as f:
		return crc32(f.read())&0xffffffff

def putCrc32(file_path, msg):
    f=open(file_path,"w")
    f.write(msg)
    f.close

# 通过random.randint(a, b)方法得到随机数字
def generate_random_str(length):
	random_str=""
	base_str="ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789!@#$%^&*()"
	n=len(base_str)-1
	for i in range(int(length)):
	    random_str+=base_str[random.randint(0,n)]  
	return random_str

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print ("Usage: python create_crc_data.py <data_length>")
        exit(-1)

    data_length = sys.argv[1]
    file_name = str(data_length) +'.dat'

    putCrc32(file_name, generate_random_str(data_length))


    checksum=getCrc32(file_name)
	
    output_file = file_name.replace('.dat','_crc32.dat')
	
    putCrc32(output_file, hex(checksum))

    print ("Reserve the crc data in %s" % output_file)

    print ("Crc:",(hex(checksum)))

    exit(0)