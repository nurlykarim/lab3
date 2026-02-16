class Circle:
    pi = 3.14159
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2


r = int(input())
c = Circle(r)
print(f"{c.area():.2f}")
