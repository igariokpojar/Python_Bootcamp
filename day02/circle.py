class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def cal_area(self):
        return Circle.pi * self.radius ** 2

    def calc_perimeter(self):
        return 2 * Circle.pi * self.radius

    def __str__(self):
        return (f"Circle radius: {self.radius}\nCircle diameter: {2 * self.radius}"
                f"\nCircle area: {self.cal_area()}\nCircle perimeter: {self.calc_perimeter()}")


circle = Circle(9)
print(circle)
