#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 15:38:31 2019

@author: Ing. Ehsan Hosseini
Project: CAN-BUS
Task: send periodic
This example exercise the periodic sending capabilities.
Expects a vcan0 interface:
    python3 -m CAN-BUS-try_04_send-periodic
"""
from __future__ import print_function

import logging
import time

logging.basicConfig(level=logging.INFO)
import can
can.rc['interface'] = 'socketcan_ctypes'

from can import Message
from can.interface import MultiRateCyclicSendTask

print(__doc__)


bustype = 'socketcan_native'
channel = 'vcan0' # can_interface

def simple_send_periodic(bus):
    """
    Sends a message every 20ms with no explicit timeout
    Sleeps for 2 seconds then stops the task.
    """
    print("Try to Starting to send a message periodic every 200ms for 10s...")
    msg = Message(arbitration_id=0x0cf02200, data=[0, 1, 3, 1, 4, 1], extended_id=False)
    task = bus.send_periodic(msg, 0.20, store_task=False)
    assert isinstance(task, can.CyclicSendTaskABC)
    time.sleep(2) # second
    
    print("Trying to change data")
    msg.data[0] = 99
    task.modify_data(msg)
    time.sleep(2)
    
    task.stop()
    print("stop cyclic send!")
    
    time.sleep(1)
    task.start()
    print('starting again')
    time.sleep(1)
    print("done")
    time.sleep(5)
    task.stop()
    
def limited_periodic_send(bus):
    print("Starting to send a message every 200ms for 4s")
    msg = can.Message(arbitration_id=0x12345678, data=[0, 0, 0, 0, 0, 0], is_extended_id=True)
    task = bus.send_periodic(msg, 0.20, 4, store_task=False)
    if not isinstance(task, can.LimitedDurationCyclicSendTaskABC):
        print("This interface doeen't sem to support!")
        task.stop()
        return
    
    time.sleep(2)
    print("Cyclic send should have stopped as duration expired")
    # Note the (finished) task will still be  tracked by the Bus
    # unless we pass 'store_task=False' to bus.send_periodic
    # alternatively calling stop removes the task from the bus
    #task.stop()

def periodic_send_with_modifying_data(bus):
    print("Starting to send a message every 200ms. Initial data is ones")
    msg = can.Message(arbitration_id=0x0cf02200, data=[1, 1, 1, 1])
    task = bus.send_periodic(msg, 0.20)
    if not isinstance(task, can.ModifiableCyclicTaskABC):
        print("This interface doesn't seem to support modification")
        task.stop()
        return
    
    time.sleep(2)
    print("Changing data of running task to begin with 99")
    msg.data[0] = 0x99
    task.modify_data(msg)
    time.sleep(2)
    
    task.stop()
    print("stopped cyclic send")
    print("Changing data of stopped task to single ff byte")
    msg.data = bytearray([0xff])
    msg.dlc = 1
    task.modify_data(msg)
    time.sleep(1)
    print("starting again")
    task.start()
    time.sleep(2)
    task.stop()
    print("done")
   
# will have to consider how to expose items like this. The socketcan
# interface will continue to support it... but the top level api won't.
    
def dual_rate_periodic_send(bus):
    """
    Send a message 10 times at 1ms intervals, then continue to send every 500ms
    """
    msg = can.Message(arbitration_id=0x123, data=[0, 1, 2, 3, 4, 5])
    print("Creating cyclic task to send message 10 times at 1ms, then every 500ms")
    task = MultiRateCyclicSendTask('vcan0', msg, 10, 0.001, 0.50)
    time.sleep(2)
    print("Changing data[0] -> 0x42")
    msg.data[0]=0x42
    task.modify_data(msg)
    time.sleep(2)
    
    task.stop()
    print("stopped cyclic send")
    
    time.sleep(2)
    
    task.start()
    print("starting again")
    time.sleep(2)
    task.stop()
    print("done hele done hele halva je done ai je dane ai je dane")

    
    
if __name__ == '__main__':
    bus = can.interface.Bus(channel=channel, bustype=bustype)
    #simple_send_periodic(bus)
    #limited_periodic_send(bus)
    periodic_send_with_modifying_data(bus)
    #dual_rate_periodic_send(bus)

