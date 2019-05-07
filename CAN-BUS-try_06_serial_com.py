#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:10:41 2019

@author: Ing. Ehsan Hosseini
Project: CAN-BUS
Task: send and recieve over serial-com linux

This example sends every second a messages over the serial interface and also
recieves incoming messages.

python -m CAN-BUS_try_06_serial_com

press ctrl+c to stop script

Expects two serial ports (/dev/ttyS10 and /dev/ttyyS11) connected to each other:
    Linux:
        To connect two ports use socat.
        sudo apt-get install socat
        sudo socat PTY,link=/dev/ttyS10 PTY,link=/dev/ttyS11
        
        Windows:
            This example was not tested on Windows. To create and connect virtual
            ports on Windows, the following software can be used:
                com0com: http://com0com.sourceforge.net/
"""

from __future__ import print_function

print(__doc__)
print(__file__)

import time
import threading

import can

# Configure can
can.rc['interface'] = 'socketcan_ctypes'
bustype = 'socketcan_native' # can_interface
bustype_serial = 'serial'
channel = 'vcan0' # channel
channel_server = '/dev/ttyS10'
channel_client = '/dev/ttyS11'


def send_cyclic(bus, msg, stop_event):
    print("Startto send a message every 5s")
    start_time = time.time()
    while not stop_event.is_set():
        msg.timestamp = time.time() - start_time
        bus.send(msg)
        print("tx: {}".format(tx_msg))
        time.sleep(5)
    print("Stopped sending messages")
    
    

def recieve(bus, stop_event):
    print("Start recieving messages")
    while not stop_event.is_set():
        rx_msg = bus.recv(1)
        if rx_msg is not None:
            print("rx: {}".format(rx_msg))
    print("Stopped recieving messages")
    
if __name__ == '__main__':
    # define Buses
    # bus transfer:
    server = can.interface.Bus(bustype=bustype, channel=channel)
    #server = can.interface.Bus(bustype=bustype_serial, channel= channel_server)
    
    # bus reciever
    client = can.interface.Bus(bustype=bustype, channel=channel)
    #client = can.interface.Bus(bustype=bustype_serial, channel=channel_client)
    
    tx_msg = can.Message(arbitration_id=0x01, data=[0x11, 0x22, 0x33, 0x44,
                                                    0x55, 0x66, 0x77, 0x88])
    
    
    # Thread for sending and recieving messages
    stop_event = threading.Event()
    t_send_cyclic = threading.Thread(target=send_cyclic, args=(server, tx_msg,
                                                               stop_event))
    
    t_recieve = threading.Thread(target=recieve, args=(client, stop_event))
    t_recieve.start()
    t_send_cyclic.start()
    
    try:
        while True:
            pass
    except KeyboardInterrupt:
        pass
    
    stop_event.set()
    server.shutdown()
    client.shutdown()
    
    print("Stopped script")

















