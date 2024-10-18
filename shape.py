import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")

    def compare_area(self, other):
        if self.area() > other.area():
            return "Площадь текущей фигуры больше, чем у другой фигуры"
        elif self.area() < other.area():
            return "Площадь текущей фигуры меньше другой фигуры"
        else:
            return "Площади равны"

    def compare_perimeter(self, other):
        if self.perimeter() > other.perimeter():
            return "Периметр текущей фигуры больше, чем у другой фигуры"
        elif self.perimeter() < other.perimeter():
            return "Периметр текущей фигуры меньше, чем у другой фигуры"
        else:
            return "Периметры равны"


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        # Предположим, что это равносторонний треугольник с периметром 3 * base
        return 3 * self.base


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


# test
square = Square(4)
rectangle = Rectangle(4, 6)
triangle = Triangle(4, 3)
circle = Circle(3)

print(square.compare_area(rectangle))
print(square.compare_perimeter(triangle))
print(circle.compare_area(triangle))
print(rectangle.compare_perimeter(circle))
