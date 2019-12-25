#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 14:15:24 2019

@author: ehsan

Python inheritance and Object-Oriented Programming OOP
the informal interafces as Shape are termed as Protocol

reference:
    http://masnun.rocks/2017/04/15/interfaces-in-python-protocols-and-abcs/
"""

# built-in modules
# Abstrtact Base Class
import abc

# Abstract Base Classes (Shape is a Protocol)
class Shape(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
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
        pass
    
    
    
    

class GeometryShape(Shape):
    # class Attributes
    shape=""
    superclass=True
    subclass = False
    # Initialize / Instantiate atrributes
    def __init__(self, shapes):
        self._shapes = shapes
        self.index = 0
        print("{} class is initiated".format(type(self).__name__)) # return class name
        #print("{} class is initiated".format(self.whoami)) # return class name

    
    def __len__(self):
        return len(self._shapes)
    
    def __contains__(self, shape):
        return shape in self._shapes
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self._shapes or self.index == len(self._shapes):
            self.index=0    # reset iterable
            raise StopIteration
        elif self.index < len(self._shapes):
            self.index += 1
            return self._shapes[self.index-1]
        
        
    def my_object_attributes(self):
        return self.__dict__
    
    def my_class_private_attributes(self):
        return self.__class__.__dict__
    
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
    
    
# ABCs and Virtual subclass
@GeometryShape.register
class Threeangle:
    shape = "Threeangle"
    pass


class Rectangle(GeometryShape):
    # class attributes
    shape = "Rectangle"
    superclass = True
    subclass = True
    # Initializing / Instantiating method
    def __init__(self, length, width):
        super().__init__(self.shape) # refer to __init__ method of super class
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
    
    geoShapes = GeometryShape(['threeangle', 'rectangle', 'square'])
    for shape in geoShapes:
        print("iterable element:", shape,'\n')
    
    
    rectangle = Rectangle(2,3)
    print("Rectangle area: %d" % rectangle.area())
    print("Rectangle perimetr: %d" % rectangle.perimeter())
    
    square = Square(4)
    print("square area: %d" % square.area())
    
    print('is square an instance of Rectangle: %s \n' % isinstance(square, Rectangle))
    print('square myShape(): ', square.myShape)
    #square.myShape('square2')
    #print('square myShape(): ', square.myShape)
    
    threeangle = Threeangle()
    print("threeangle shape:", threeangle.shape)
    print("is class Threeangle subclass of GeometryShape: {}".format(issubclass(Threeangle, GeometryShape)) )
    print("is object threeangle instance of GeometryShape: {}".format(isinstance(threeangle, GeometryShape)) )
    
    isinstance(geoShapes, abc.ABC)
    GeometryShape.whoami(GeometryShape)



