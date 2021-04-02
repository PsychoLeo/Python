from math import pi

class Rectangle :

    def __init__(self, sideA=0, sideB=0):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB
  
    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)

class Circle :

    def __init__ (self, radius) :
        self.radius = radius
        self.area = pi*radius**2
        self.perimeter = 2*pi*radius
        
    def getPerimeter (self):
        return self.perimeter
        
    def getArea (self) :
        return self.area