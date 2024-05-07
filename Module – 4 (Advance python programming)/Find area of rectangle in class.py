'''• Write a Python class named Rectangle constructed by a length and 
width and a method which will compute the area of a rectangle'''

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Find(self):
        print("Area of the reactangle : ",self.length * self.width)


r1= Rectangle(5, 3)
r1.Find()
