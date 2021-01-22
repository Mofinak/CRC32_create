#!/usr/bin/python
# -*- coding: UTF-8 -*-

from zlib import crc32
import os
import sys
import random

def getCrc32(filename):
	with open(filename, 'rb') as f:
		return crc32(f.read())&0xffffffff

def putCrc32(file_name, data):
    f=open(file_name,"w")
    f.write(data)
    f.close

# 通过random.randint(a, b)方法得到随机数字
def generate_random_str(length):

    random_str=""
    # base_str="ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789!@#$%^&*"
    base_str="ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"
    print(type(base_str))
    print ("base_str %s" % len(base_str))
    n=len(base_str)-1
    # n=61

    for i in range(int(length)):
        random_str+=base_str[random.randint(0,n)]  

    return random_str

if __name__ == '__main__':

    if len(sys.argv) < 2:
        print ("Usage: python create_crc_data.py <data_length>")
        exit(-1)

    if (False == os.path.isdir('data')):
        os.mkdir('data')

    data_length = sys.argv[1]

    #todo 参数检查

    if (data_length.endswith('b') | data_length.endswith('B')):
        data_len = data_length[0:-1]
        lenth = int(data_len)
    elif (data_length.endswith('k') | data_length.endswith('K')):
        data_len = data_length[0:-1]
        print (data_len)
        lenth = int(data_len)*1024
    elif (data_length.endswith('m') | data_length.endswith('M')):
        data_len = data_length[0:-1]
        lenth = int(data_len)*1024*1024
    else:
        lenth = int(data_length)

    print ("data length is %s----%s byte" % (data_length, lenth))
    
    # name the input file
    file_name = "data/"+ str(data_length) +'.dat'
    print("input_file_name  %s" % file_name)

    #reserve the random data file
    putCrc32(file_name, generate_random_str(lenth))

    # CRC32 calculation
    checksum=getCrc32(file_name)
	
    #name the output file
    output_file = file_name.replace('.dat','_crc32.dat')
	
    #reserve the crc32 result
    putCrc32(output_file, hex(checksum))

    print ("Reserve crc data in %s" % output_file)

    print ("Crc:",(hex(checksum)))

    exit(0)