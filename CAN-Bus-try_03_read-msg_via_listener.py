#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:10:27 2019

@author: Ing. Ehsan Hosseini
Project: CAN-BUS
Task: read messages via listener -> two type listener

Note:    
    A Listener can be used in two ways.
    The Listener wish to register to recieve notifications of new message
    on the bus.
"""
from __future__ import print_function
import time
import can

print(__doc__)
print(__file__)

bustype = 'socketcan_native'
channel = 'vcan0' # can_interface

def read_msg_listener(can_interface):
    """
    basic listener
    """
    bus = can.interface.Bus(channel=can_interface, bustype=bustype)
    listener = can.Listener()
    """
    msg = bus.recv()
    
    if msg is None:
        print("Timeout accured, no message is recieved.")
    else:
        print(msg)
    """
    
    
    
    
    reader = can.BufferedReader() # reader is a Listener
    notifier = can.Notifier(bus, [reader])
    #time.sleep(10)
    msg = None
    while msg is None:
        msg = reader.get_message() # as a parameter can be Timeout -> 
        # now either call
        print(msg)
        listener(msg)
        # or
        listener.on_message_received(msg)
        print(msg)
        
    time.sleep(10)
    listener.stop()

def read_iterate_msg(bus=None):
    # create a bus instance
    # many other interfaces are supported as well
    if bus is None:
        bus = can.Bus(interface='socketcan',
                      channel='vcan0',
                      recieve_own_messages=True)
    
    
    #send a message
    """
    message = can.Message(arbitration_id=1234, is_extended_id=True,
                          data=[0x11, 0x22, 0x33])
    bus.send(message, timeout=0.2)
    """
    
    # iterate over received messages
    """
    for msg in bus:
        print("{}: {}".format(msg.arbitration_id, msg.data))
    """
    
    # or use an asynchronous notifier
    notifier = can.Notifier(bus, [can.Logger("recorded.log"), can.Printer()])
    
    

if __name__ == '__main__':
    read_msg_listener(can_interface=channel)
    
    # read messages via can.Notifier and save in file -> "recorded.log"
    read_iterate_msg()

