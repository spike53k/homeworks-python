class Drobi:
    def __init__(self, a=1, b=1):
        self.a = a
        self.b = b
    def show(self):
        print(f"{self.a}/{self.b}")

    def get_a(self):
        return self.a
    def set_a(self, a):
        self.a = a

    def get_b(self):
        return self.b
    def set_b(self, b):
        self.b = b

    def plus(self, f2):
        return Drobi(self.a * f2.b + f2.a * self.b, self.b * f2.b)
    def minus(self, f2):
        return Drobi(self.a * f2.b - f2.a * self.b, self.b * f2.b)
    def multiply(self, f2):
        return Drobi(self.a * f2.a, self.b * f2.b)
    def divide(self, f2):
        return Drobi(self.a * f2.b, self.b * f2.a)

f1 = Drobi(1, 2)
f2 = Drobi(2, 3)

f1.plus(f2).show()
f1.minus(f2).show()