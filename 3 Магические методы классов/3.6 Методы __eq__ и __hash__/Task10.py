from math import sqrt

class Validator(object):
    def validate(self, value):
        if not isinstance(value, (int, float)) or value <= 0:
            return False
        else:
            return True

class SideTriangle(object):
    def __init__(self, validator=Validator()):
        self.validator = validator

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance,self.name, None)

    def __set__(self, instance, value):
        if self.validator.validate(value):
            setattr(instance, self.name, value)
        else:
            raise ValueError("длины сторон треугольника должны быть положительными числами")

class Triangle(object):
    a = SideTriangle()
    b = SideTriangle()
    c = SideTriangle()

    def __init__(self, a, b, c):
        super(Triangle, self).__init__()
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_triangle(a,b,c):
        if a and b and c:
            return a < b + c and b < a + c and c < a + b
        return True

    def __setattr__(self, key, value):
        if (key == 'a' and not self.is_triangle(value, self.b, self.c)) or \
            (key == 'b' and not self.is_triangle(self.a, value, self.c)) or \
            (key == 'c' and not self.is_triangle(self.a, self.b, value)):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

        super().__setattr__(key, value)

    def __len__(self):
        return int(self.a + self.b + self.c)

    def __call__(self):
        if not (self.a and self.b and self.c):
            return
        p = (self.a + self.b + self.c) *0.5
        s = sqrt(p  * (p - self.a) * (p-self.b) * (p-self.c))
        return s
