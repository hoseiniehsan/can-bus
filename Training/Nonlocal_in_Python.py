#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 18:51:20 2019

@author: Ing. Ehsan Hosseini
Note:
    Nonlocal in Python
    The use of 'nonlocal' keyword is very much similar to the 'global'.
    'nonlocal' is used to declare that a variable inside a nested function
    (function inside a function) is not local to it, meaning it lies in the
    outer inclosing function. If we need to modify the value of a non-local
    variable inside a nested function , then we must declare it with 'nonlocal'.
    Otherweise a local varibale with that name is created inside the nested
    function. Following example will help you clarify this.
"""

import sys

if sys.version_info < (3, 2, 0):
    raise EnvironmentError("Python 3.2 or later is required!")
    
print(__doc__)
print(__file__)
# Ctrl+l -> Goto line
# Strg+l

# This is the outer enclosing func
def outer_function():
    a = 5
    # This is the nested func
    def inner_function():
        nonlocal a
        a = 10
        print("\n Inner function value 'a' is:", a)
    
    # Call inner function:
    #inner_function()
    print("\n Outer function value 'a' is:", a)
    return inner_function
    

def make_multiplier_of(x):
    def multiplier(n):
        #print("x is: %d, n is: %d, %d * %d= %d" % (x, n, x, n, x*n))
        return x * n
    return multiplier

if __name__ == '__main__':
    #outer_function()
    # Call inner function
    inner = outer_function()
    inner()
    
    # Multiplier of 3 -> x = 3
    times3 = make_multiplier_of(3)
    # Output in Console: 3
    times3.__closure__[0].cell_contents
    
    # Multiplier of 5 -> x = 5
    times5 = make_multiplier_of(5)
    
    # Output: 21 -> times3 * 7 -< n=7
    print(times3(7))
    
    # Output: 15
    print(times5(3))
    
    # Output: 30
    print(times5(times3(2)))

