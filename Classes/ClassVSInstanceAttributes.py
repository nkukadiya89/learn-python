# Class vs Instance Attributes

class Point:
    default_color = "white"

    def __init__(self,x,y):
       self.x = x
       self.y = y
    
    def disp(self):
         print(f"constructor value {self.x} , {self.y}")

default_color = "green"

point = Point(2,5)
point.disp()

#class attribute
print(Point.default_color)

#instance attribute
print(point.default_color)

