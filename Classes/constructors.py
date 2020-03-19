#Constructor in Python

class Point:
  
    #Constructor define using __init__ method
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def disp(self):
        print(f"class {self.x},{self.y}")

point = Point(2,5)
print(point.x)
point.disp()        