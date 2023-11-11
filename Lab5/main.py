import math


# Create a class hierarchy for shapes, starting with a base class Shape.
# Then, create subclasses like Circle, Rectangle, and Triangle. Implement methods
# to calculate area and perimeter for each shape.

class Shape:
    def __init__(self, coord_x_of_center, coord_y_of_center):
        self.center_coord = (coord_x_of_center, coord_y_of_center)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)

        self.no_of_edges = 0
        self.radius = radius

    def area(self):
        return self.radius ** 2 * math.pi

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, x, y, height, width):
        super().__init__(x, y)
        self.no_of_edges = 4
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def length_of_diagonal(self):
        return (self.height ** 2 + self.width ** 2) ** (1/2)


class Triangle(Shape):
    def __init__(self, x, y, len_a, len_b, len_c):
        super().__init__(x, y)
        self.no_of_edges = 3
        self.edges = [len_a, len_b, len_c]

    def area(self):
        s = self.perimeter()/2
        return ((s - self.edges[0]) * (s - self.edges[1]) * (s - self.edges[2]) * s) ** (1 / 2)

    def perimeter(self):
        return self.edges[0] + self.edges[1] + self.edges[2]

    def is_right_triangle(self):
        longest_edge = max(self.edges)
        s = 0
        for edge in self.edges:
            if edge != longest_edge:
                s += edge ** 2
        return longest_edge ** 2 == s


