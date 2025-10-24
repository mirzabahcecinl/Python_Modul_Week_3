class Shape:
    def __init__(self,height,width):
        self.height = height
        self.width = width
class Rectangle(Shape):
    def __init__(self,height,width):
        super().__init__(height,width)
    def area(self):
            return self.height * self.width
class Square(Shape):
    def __init__(self,side):
        super().__init__(side,side)
    def area(self):
        return self.height * self.width
rect=Rectangle(10,15)
print(rect.area())
sqr=Square(10)
print(sqr.area())



