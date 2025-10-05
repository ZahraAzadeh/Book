import math

# کلاس پایه
class Shape:
    def area(self):
        raise NotImplementedError("متد area باید در کلاس‌های فرزند بازنویسی شود.")

# کلاس مستطیل
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# کلاس دایره
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
