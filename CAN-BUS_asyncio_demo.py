#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 20:17:22 2019

@author: Ing. Ehsan Hosseini
Project: CAN-BUS
Task: send periodic
This example exercise the asynchron io messgae
Expects a vcan0 interface:
    python3 -m CAN-BUS-try_05_asyncio_demo
    
"""

from __future__ import print_function

import time
import can
import asyncio

print(__doc__)
print(__file__)

can.rc['interface'] = 'socketcan'
bustype = 'socketcan_native'
channel = 'vcan0'

def print_message(msg):
    """ Regulare callback function. Can also be coroutine."""
    print(msg)
    
async def main():
    can0 = can.Bus(channel=channel, bustype=bustype, recieved_own_messages=True)
    reader = can.AsyncBufferedReader()
    logger = can.Logger('logfile.asc')
    
    listener = [
            print_message,  # Callback function
            reader,         # AsyncBufferedReader() listener
            logger          # Regular Listener object
            ]
    # Create Notifier with an explicit loop to use for scheduling of callbacks
    loop = asyncio.get_event_loop()
    notifier = can.Notifier(can0, listener, loop=loop)
    # Start sending first message
    message = can.Message(arbitration_id=0, extended_id=True)
    can0.send(message)
    
    print('Bouncing 10 messages...')
    for _ in range(10):
        # Wait for next message from AsyncBufferedReader
        msg = await reader.get_message()
        # Delay response
        await asyncio.sleep(0.5)
        msg.arbitration_id += 1
        can0.send(msg)
    
    # Wait for last message to arrive
    await reader.get_message()
    time.sleep(2.0)
    print('Done!')
    
    
    # Clean-up
    notifier.stop()
    can0.shutdown()
    

#if __name__ == '__main__':
    
# Get the default event loop
loop = asyncio.get_event_loop()
# Run until main coroutine finishes
loop.run_until_complete(main())
loop.close()
