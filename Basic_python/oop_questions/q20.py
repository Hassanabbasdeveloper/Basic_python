# Create Point class
class Point:

    # Constructor
    def __init__(self, x, y):

        # Store x-coordinate
        self.x = x

        # Store y-coordinate
        self.y = y


# Create Line class
class Line:

    # Constructor
    def __init__(self, a, b, c):

        # Store coefficient A
        self.a = a

        # Store coefficient B
        self.b = b

        # Store coefficient C
        self.c = c

    # Check whether point lies on line
    def is_point_on_line(self, point_obj):

        # Apply equation Ax + By + C = 0
        return (self.a * point_obj.x) + (self.b * point_obj.y) + self.c == 0


# Create Line object
line = Line(1, 1, -2)

# Create Point object
pt = Point(1, 1)

# Check point
print(line.is_point_on_line(pt))