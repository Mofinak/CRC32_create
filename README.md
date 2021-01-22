# CRC32_create

#### This project is to create vector file for xilinx xrt mutiprocess test.

#### create_crc_data.py
##### 1 create specify length random test vector(file)
##### 2 calculate the crc32
##### 3 save the crc result to file in the data/ folder with the .dat suffix
##### Usage: python create_crc_data.py <data_length>
##### data_length could be byte//Kilobyte/Megabyte
##### example:
##### python create_crc_data.py 64    --create a 64byte file and calculate crc
##### python create_crc_data.py 2K    --create a 2Kbyte file and calculate crc
##### python create_crc_data.py 5M    --create a 5Mbyte file and calculate crc

#### create_deploy_pic_crc.py
##### calculate the input .jpg file crc32 result, the result will be reserved with _crc32.dat subffix
##### the test vector reserved in the testbench/ folder
##### Usage: python create_deploy_pic_crc.py <input_file>
##### example:
##### python create_deploy_pic_crc.py testbench/800p_1.jpg
