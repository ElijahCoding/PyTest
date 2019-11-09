class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return "Rectangle(%.1f, %.1f)" % (self.side_a, self.side_b)


class Circle:
    def __init(self, radius):
        self.radius = radius