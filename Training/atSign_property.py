#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 18:33:08 2019

@author: Ing. Ehsan Hosseini
Projekt: Training
Task:concept of @property

Note:
    Finally note that, the actual temperature value is stored in the private 
    variable _temperature. The attribute temperature is a property object which
    provides interface to this private variable.
"""

#ToDo
print(__doc__)

import sys

if sys.version_info < (3, 2, 0): # (major=3, minor= 2, micro= 0)
    raise EnvironmentError("Python version 3.2 or later required!")
    
class Celsius(object):
    def __init__(self, temperature=0):
        #self._temperature = temperature
        self.temperature=temperature
        #self.set_temperature(temperature)
        print("temperature is %s" % temperature)
        print("_temperature is %s" % self._temperature)
        print("self.temperature is %s" % self.temperature)
        print("Initialized class")
        
    
    def to_farenheit(self):
        #return (self.get_temperature() * 1.8 ) + 32
        return (self.temperature * 1.8) + 32
    
    """
    def get_temperature(self):
        # underscore (_) at the beginning is used to denote private variables
        print("Getting Value")
        # _temperature is only a inteface to temperature
        return self._temperature
        
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not pssible")
        print("Setting Value")
        self._temperature = value
        
    """
    
    # Define getter property
    @property
    def temperature(self):
        print("Getting Value new Method")
        return self._temperature
    
    # Define setter property
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not pssible")
        print("Setting Value new method")
        self._temperature = value
        
    # Define a property has two way that are both of them aquivalent:
    
    # First way:
    
    # tempreture is a attribute that has two func get and set -> property(fget, fset, fdel, doc)
    #temperature = property(get_temperature, set_temperature, doc="temp_attrib")
    
    
    # Second way:
    """
    # Make empty property
    temperature = property()
    # assign fget
    temperature = temperature.getter = get_temperature
    # assign fset
    temperature = temperature.setter = set_temperature
    """
    
if __name__ == '__main__' :
    # Create new object
    man = Celsius(3)
    
    # Set temperature
    #man.temperature = 37
    
    # Get temperature
    print("man.temperature: %.3f" % man.temperature)
    
    # Get degrees Farenheit
    print(man.to_farenheit())

