import math


class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Either radius or diameter must be provided.")

    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    def __repr__(self):
        return f"Circle(radius={self.radius}, diameter={self.diameter})"

    def __add__(self, other):
        if isinstance(other, Circle):
            return Circle(radius=self.radius + other.radius)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.radius > other.radius
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    @staticmethod
    def sort_circles(circles):
        return sorted(circles, key=lambda circle: circle.radius)


circle1 = Circle(radius=5)
circle2 = Circle(diameter=10)
circle3 = Circle(radius=7)

print(f"Area of circle1: {circle1.area()}")

print(circle1)

circle_sum = circle1 + circle2
print(f"Sum of circle1 and circle2: {circle_sum}")

print(f"Is circle1 greater than circle2? {circle1 > circle2}")
print(f"Is circle1 equal to circle2? {circle1 == circle2}")

sorted_circles = Circle.sort_circles([circle1, circle2, circle3])
print("Sorted circles by radius:")
for circle in sorted_circles:
    print(circle)
