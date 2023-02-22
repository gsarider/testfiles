#!/usr/bin/env python3

import sys
import time
import config
from time import sleep


#config={'SERVER': '192.168.147.0',
#         'K4_IP': '192.168.147.20',
#         'PORT': 9200 ,
#         'TIMEOUT': 5 }

global jaja
jaja=""

# use something like this for the K4 ip addr/port
def main():
    ''' main body'''
    print("zero")
    
    if  config.SERVER:
        K4IP = config.SERVER
        print (K4IP)
        pport=config.PORT
        print(config.PORT, pport)
        print("jeden")
        time.sleep(5)
        print('dwa')
        sleep(5)
        print("trzy")
        sys.exit()
    else:
        K4IP = '192.168.147.20'
        print(K4IP)

main()
