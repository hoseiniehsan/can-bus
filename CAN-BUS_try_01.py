#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 11:25:28 2019

@author: Ing. Ehsan Hosseini
Project: CAN-BUS
This example show how sending a single message works.
"""
from __future__ import print_function

import sys

'''
sys.path.append(['', '/home/ehsan/anaconda3/lib/python36.zip', '/home/ehsan/anaconda3/lib/python3.6',\
                 '/home/ehsan/anaconda3/lib/python3.6/lib-dynload',\
                 '/home/ehsan/anaconda3/lib/python3.6/site-packages',\
                 '/home/ehsan/anaconda3/'])
'''



print(__doc__)
print(__file__)
print(sys.path)

import can
print('\nCAN-BUS Version: %s' % can.__version__)



def send_one():
    
    # this uses the defaults configration (for example the config file)
    # see http://python-can.readthedocs.io/en/latest/configuration.html
    bus = can.interface.Bus()
    
    # Using specific buses works similar:
    #bus  = can.interface.Bus(bustype='socketcan', channel='vcan0', bitrate=250000)
    #bus = can.interface.Bus(bustype='pcan', channel='PCAN_USBBUS1', bitrate=250000)
    #bus = can.interface.Bus(bustype='ixxat', channel=0, bitrate=250000)
    #bus = can.interface.Bus(bustype='vector', app_name= 'CANanalyzer', channel=0, bitrate=250000)
    # ...
    
    msg = can.Message(arbitration_id=0xc0ffee,
                      data=[0, 25, 0, 1, 3, 1, 4, 1],
                      extended_id=True)
    
    try:
        bus.send(msg)
        print("Message sent on {}".format(bus.channel_info))
    except can.CanError:
        print("Message NOT sent")
        
if __name__ == "__main__":
    send_one()

