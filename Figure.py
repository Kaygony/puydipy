class Figure:
    pass


class Point(Figure):
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = r


class Polygon(Figure):
    def __init__(self, *points):
        self.points = points


class Line(Polygon):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)


class Triangle(Polygon):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)


class IsoscelesTriangle(Triangle):
    def __init__(self, p1, p2, l):
        a = (pow(p1.y, 2) - pow(p2.y, 2)) / (p1.y - p2.y)
        b = p1.x + pow(pow(l, 2) - pow(a - p1.y, 2), 1/2)
        if pow(b - p1.x, 2) - pow(a - p1.y, 2) == pow(b - p2.x, 2) - pow(a - p2.y, 2) == pow(l, 2):
            p3 = Point(b, a)
            super().__init__(p1, p2, p3)
        elif pow(-1*b - p1.x, 2) - pow(a - p1.y, 2) == pow(-1*b - p2.x, 2) - pow(a - p2.y, 2) == pow(l, 2):
            p3 = Point(-b, a)
            super().__init__(p1, p2, p3)
        elif pow(b - p1.x, 2) - pow(-1 * a - p1.y, 2) == pow(b - p2.x, 2) - pow(-1 * a - p2.y, 2) == pow(l, 2):
            p3 = Point(b, -a)
            super().__init__(p1, p2, p3)
        elif pow(-1 * b - p1.x, 2) - pow(-1 * a - p1.y, 2) == pow(-1 * b - p2.x, 2) - pow(-1 * a - p2.y, 2) == pow(l, 2):
            p3 = Point(-b, -a)
            super().__init__(p1, p2, p3)


class Rectangle(Polygon):
    def __init__(self, l_d, r_u):
        a = 0
        b = 0
        if l_d.y < 0:
            a = -1 * l_d.y
        elif r_u.y < 0:
            b = -1 * r_u.y
        sum = a + b
        c = l_d.x
        d = l_d.y + sum
        l_u = Point(c, d)
        if l_d.x < 0:
            a = -1 * l_d.x
        elif r_u.x < 0:
            b = -1 * r_u.x
        sum = a + b
        d = l_d.x + sum
        c = l_d.y
        r_d = Point(c, d)
        super().__init__(l_d, l_u, r_d, r_u)


class Square(Rectangle):
    def __init__(self, p, l):
        z = Point(p.x + l, p.y + l)
        super().__init__(p, z)







