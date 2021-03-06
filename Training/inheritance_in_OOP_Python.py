#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:15:24 2019

@author: ehsan

Python inheritance and Object-Oriented Programming OOP
"""

import abc

# Abstract Base Classes
class Shape(abc.ABC):
    @abc.abstractmethod
    def __init(self):
        pass
    
    @abc.abstractmethod
    def __len__(self):
        pass
        #return self
    
    @abc.abstractmethod
    def __contains__(self):
        pass
    
    @abc.abstractmethod
    def __iter__(self):
        pass
    
    @abc.abstractmethod
    def __next__(self):
    
    
    
    

class GeometryShape(Shape):
    # class Attributes
    shape=""
    superclass=True
    subclass = False
    # Initialize / Instantiate atrributes
    def __init__(self):
        print("{} class is initiated".format(type(self).__name__)) # return class name
    
    # instance methods
    def whoami(self):
        return type(self).__name__
    
    def whereami(self):
        return self.__class__
        
    def area(self):
        pass
    
    def perimeter(self):
        pass
    
    def myParent(self):
        return super().__name__
    
    @property
    def myShape(self):
        return self.shape
    
    @myShape.setter
    def myShape(self, newshape=''):
        self.shape = newshape
        return True


class Rectangle(GeometryShape):
    # class attributes
    shape = "Rectangle"
    superclass = True
    subclass = True
    # Initializing / Instantiating method
    def __init__(self, length, width):
        super().__init__() # refer to __init__ method of super class
        self.length = length
        self.width = width
        
    # instance methods
    def area(self):
        return self.length*2 + self.width*2
    
    def perimeter(self):
        return self.length * self.width
    
class Square(Rectangle):
    # class attribute
    shape = "Square"
    superclass = False
    subclass = True
    # Initializing
    def __init__(self, length):
        super().__init__(length, length)
        





# Main
if __name__ == '__main__':
    rectangle = Rectangle(2,3)
    print("Rectangle area: %d" % rectangle.area())
    print("Rectangle perimetr: %d" % rectangle.perimeter())
    
    square = Square(4)
    print("square area: %d" % square.area())
    
    print('is square an instance of Rectangle: %s \n' % isinstance(square, Rectangle))
    print('square myShape(): ', square.myShape)
    square.myShape('square2')
    #print('square myShape(): ', square.myShape)



