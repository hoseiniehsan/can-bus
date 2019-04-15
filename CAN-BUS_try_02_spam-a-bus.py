#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 15:53:41 2019

@author: Ing. Ehsan Hosseini
Project: CAN-BUS
spam a bus via vcan0 ad monitor with Wireshark
"""

from __future__ import print_function

import can
import sys
import time

print(__doc__)
print(__file__)
print(sys.path)
print('\nCAN-BUS Version: %s' % can.__version__)

bustype = 'socketcan_native'
channel = 'vcan0' # can_interface

def producer(id):
    """:param id: SPam the bus with messages includin the data id ."""
    bus = can.interface.Bus(interface='socketcan', channel=channel, bustype=bustype)
    for i in range(5):
        msg = can.Message(arbitration_id=0xc0ffee, data=[id, i, 0, 1, 3, 1, 4, 1],\
                          extended_id=False)
        time.sleep(1.0)
        bus.send(msg)
        print(msg)
    # Issue #3: Need to keep running to ensure the writing threads stay alive. ?
    time.sleep(1.0)
    
    return bus

def messages(bus):
    # iterate over recieved messages
    for message in bus:
        print("{}: {}".format(message.arbitration_id, message.data))

def read_msg(can_channel):
    bus = can.interface.Bus(can_channel, bustype=bustype)
    message = bus.recv(1.0)
    for msg in can.interface.Bus('vcan0'):
        print(msg)
    
if __name__ == "__main__":
    bus = producer(6)
    messages(bus)
    #read_msg(can_interface='vcan0')
    



