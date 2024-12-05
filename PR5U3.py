class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length

shape = Shape()
print(f"Area of Shape: {shape.area()}")

length = float(input("Enter the side length of the square: "))
square = Square(length)
print(f"Area of Square: {square.area()}")
