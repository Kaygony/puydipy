import math
from pygame import draw


class Figure:
    def draw(self, game_display, color):
        raise NotImplementedError


class Point(Figure):
    def __init__(self, x, y):
        self.x = round(x)
        self.y = round(y)

    def __repr__(self):
        return '<Point({0}, {1})>'.format(self.x, self.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)

    def draw(self, game_display, color):
        draw.circle(game_display, color, (self.x, self.y), 1)


class Circle(Point):
    def __init__(self, x, y, r):
        super().__init__(x, y)
        self.r = round(r)

    def draw(self, game_display, color):
        draw.circle(game_display, color, (self.x, self.y), self.r)


class Polygon(Figure):
    def __init__(self, *points):
        self.points = points

    def __repr__(self):
        return '<{0}{1} figure>'.format(self.__class__.__name__, self.points)

    def draw(self, game_display, color):
        game_points = [[point.x, point.y] for point in self.points]
        draw.polugon(game_display, color, game_points)


class Line(Figure):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return '<Line({0}, {1}))>'.format(self.p1, self.p2)

    def __add__(self, other):
        return Line(Point(self.p1.x, self.p1.y),
                    Point(self.p2.x + (other.p2.x - other.p1.x), self.p2.y + (other.p2.y - other.p1.y)))

    def __sub__(self, other):
        return Line(Point(self.p1.x, self.p1.y),
                    Point(self.p2.x - other.p2.x + other.p1.x, self.p2.y - other.p2.y + other.p1.y))

    def __abs__(self):
        return ((self.p2.x - self.p1.x) ** 2 + (self.p2.y - self.p1.y) ** 2) ** (1/2)

    def draw(self, game_display, color):
        draw.line(game_display, color, [self.p1.x, self.p1.y], [self.p2.x, self.p2.y])


class Triangle(Polygon):
    def __init__(self, p1, p2, p3):
        super().__init__(p1, p2, p3)


class IsoscelesTriangle(Triangle):
    def __init__(self, p1, p2, l):
        p2.x = p2.x - p1.x
        p2.y = p2.y - p1.y
        p1.x = 0
        p1.y = 0
        c = (-p2.x ** 2 - p2.y ** 2) / (-2)
        if p2.x != 0:
            a = p2.y ** 2 + p2.x ** 2
            b = -2 * p2.y * c
            e = c ** 2 - l ** 2 * p2.x ** 2
            d = b ** 2 - 4 * a * e
            m = (-b + d ** (1 / 2)) / (2 * a)
            n = (c - m * p2.y) / p2.x
        else:
            m = c / p2.y
            n = (l ** 2 - (c ** 2) / p2.y ** 2) ** (1 / 2)
        p3 = Point(n, m)
        super().__init__(p1, p2, p3)


class Rectangle(Polygon):
    def __init__(self, l_d, r_u):
        l_u = Point(l_d.x, r_u.y)
        r_d = Point(r_u.x, l_d.x)
        super().__init__(l_d, l_u, r_d, r_u)


class Square(Rectangle):
    def __init__(self, p, l):
        l_d = p
        r_u = Point(p.x + l, p.y + l)
        super().__init__(l_d, r_u)

class EquilateralPolygon(Polygon):
    def __init__(self, center_point, r, vertices):
        self.r = round(r)
        points = []
        angles = 360 / vertices
        for n in range(vertices):
            angle = angles * n
            points.append(Point(center_point.x + math.cos(math.radians(angle)) * r,
                                center_point.y + math.sin(math.radians(angle)) * r))
        super().__init__(*points)