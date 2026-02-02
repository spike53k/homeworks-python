import math

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector ({self.x}, {self.y})"

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

v1 = Vector2D(2, 4)
v2 = Vector2D(1, 2)
print(v1 + v2)
print(v1 - v2)
print(v1.length())
print(v1)
