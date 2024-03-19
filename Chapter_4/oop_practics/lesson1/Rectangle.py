class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def display(self):
        print(f'{self.length}, {self.width}, S = {self.perimeter()}, P = {self.area()}')


x1 = Rectangle(12, 90)
x1.display()
