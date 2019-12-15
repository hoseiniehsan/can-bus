#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  7 20:20:17 2019

@author: Ing. Ehsan Hosseini
Projekt: Training
Task: Python Decorators

Note:
    A decorator takes in a function, adds some functionality and returns it.
    In this article, you will learn how you can create a decorators and why 
    you should use it.
    resource: https://www.programiz.com/python-programming/decorator
"""

import sys

if sys.version_info < (3, 2, 0):
    raise EnvironmentError("Python version 3.2 or later required!")

#TODO implemment python Decorators
print(__doc__)
print(__file__)



""" #1 """
def prnt(msg):
    print("\n %s" % msg)
""" Ende #1 """



""" #2 Higher order function"""
def inc(x):
    #print("\n x is %.2f, new increased x is %.3f" % (x, x+1))
    return x + 1

def dec(x):
    #print("\n x is %.2f, new decreased x is %.3f" % (x, x-1))
    return x - 1

def operat(func, x):
    result = func(x)
    print("\n input is %.2f, result is %.3f" % (x, result))
    return result

# Second way
def op_inc_dec(func):
    def inner(x):
        print("\n operator inc_dec with @decorator_func")
        print("\n x is %.2f, return value is %.3f" % (x, func(x)))
        #return func(x) # this return is in this example optional, because func
        # is one time already called above in print func
    return inner

@op_inc_dec
def decreaser(x):
    print("x-1 is ", x-1)
    return x-1

@op_inc_dec
def increaser(x):
    print("x+1 is ", x+1)
    return x+1
""" Ende #2 Higher order function """

# Call decreaser
decreaser(10)
# Call increaser
increaser(12)




""" #3 A function can return another function """
def is_called(msg):
    # is_returned is a neted function which is defined and returned, each time
    # We call is_called()
    def is_returned():
        print("\n func is_returned printed: %s" %msg)
    return is_returned
""" Ende #3 """


""" #4 Functions and methods are called 'callable' as they can be called """
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

#def ordinary():
#    print("I am ordinary")
""" Ende #4 """

""" #5 @func"""
# Use the @ symbol along with the name of the decorator function and place it 
# above the definition of the function to be decorated.
@make_pretty
def ordinary():
    print("I am ordinary with @func")
# is equivalent to
# ordinary = make_pretty(ordinary)
""" Ende #5 """

""" #6 Decorating functions with Parameters """
def smart_divide(func):
    def inner(a, b):
        print("\n I am going to divide", a, "and", b)
        if b==0:
            print("\n Cannot divide %d/%d, beacause b is 0 and it return" % (a,b))
            return
        return func(a,b)
    return inner

@smart_divide
def divide(a,b):
    return a/b
""" Ende #6 """

# Call divide
print(divide(2,6))
print(divide(4,0))




""" #7 Chaning Decorators in Python """
# Using tuple and Dict as *args,**kwargs

def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        #func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner

@star
@percent
def printer(msg):
    print(msg)

    
# Call printer
printer("Hello star and percent")

# is equivalent to:
"""
printer = star(percent(printer))
printer("Hello star and percent")
"""

""" Ende #7 """


if __name__ == "__main__":
    prnt("Test")
    
    prnt2 = prnt
    prnt2("Test2")
    
    # Function can be passed as arguments to another function
    # Higher order function: such function that takes other functions as
    # Arguments are also called "Higher order function"
    
    
    result = operat(inc, 2)
    result = operat(dec, result)
    
    operat(inc, 6)
    operat(dec, 8.9)
    
    # A function can return another function, function returned another func
    # As returned value
    is_called("is_called") # returned Not
    new_is_called = is_called("new_is_called") # returned Value is a Func
    new_is_called()
    
    """ #4"""
    # Output: "I am ordinary"
    #ordinary()
    
    # let's decorate this ordinary function
    #pretty = make_pretty(ordinary)
    #pretty()
    
    # second way is to decorae a function and reasign it
    #ordinary = make_pretty(ordinary)
    #
    ordinary()
    """ In the example shown above, make_pretty() is a decorator """
    """ Ende #4 """
    
    
    
    
    
    
    