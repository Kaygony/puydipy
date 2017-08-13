import math

import pygame

import colors


class Drawable:
    def draw(self, game_display):
        raise NotImplementedError


class Figure(Drawable):
    def __init__(self, color=None):
        if not color:
            color = colors.BLACK
        self.color = color


class Point(Figure):
    def __init__(self, x, y, color=None):
        self.x = round(x)
        self.y = round(y)
        self.coords = (self.x, self.y)
        super().__init__(color)

    def __repr__(self):
        return '<Point({0}, {1})>'.format(self.x, self.y)

    def __mul__(self, n):
        return Point(self.x * n, self.y * n)

    def __truediv__(self, n):
        return Point(self.x / n, self.y / n)

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def draw(self, game_display):
        pygame.draw.circle(game_display, self.color, self.coords, 1)


class Circle(Point):
    def __init__(self, x, y, r, color=None):
        self.r = round(r)
        if self.r <= 0:
            raise ValueError('Radius must be 1 or higher')
        super().__init__(x, y, color)

    def draw(self, game_display):
        pygame.draw.circle(game_display, self.color, self.coords, self.r)


class Polygon(Figure):
    def __init__(self, *points, color=None):
        self.points = points
        if len(points) < 3:
            raise ValueError('Polygon must have 3 or more vertices')
        super().__init__(color)

    def __repr__(self):
        return '<{0}{1} figure>'.format(self.__class__.__name__, self.points)

    def draw(self, game_display):
        pygame.draw.polygon(game_display, self.color, [point.coords for point in self.points[:-1]])


class Line(Figure):
    def __init__(self, start, end, color=None):
        self.start = start
        self.end = end
        super().__init__(color)

    def __repr__(self):
        return '<Line({0}, {1}))>'.format(self.start, self.end)

    def __add__(self, other):
        return Line(Point(self.start.x, self.start.y),
                    Point(self.end.x + (other.end.x - other.start.x), self.end.y + (other.end.y - other.start.y)))

    def __sub__(self, other):
        return Line(Point(self.start.x, self.start.y),
                    Point(self.end.x - other.end.x + other.start.x, self.end.y - other.end.y + other.start.y))

    def __abs__(self):
        return ((self.end.x - self.start.x) ** 2 + (self.end.y - self.start.y) ** 2) ** (1/2)

    def __eq__(self, l):
        return self.start == l.start and self.end == l.end

    def draw(self, game_display):
        pygame.draw.line(game_display, self.color, self.start.coords, self.end.coords)


class Triangle(Polygon):
    def __init__(self, p1, p2, p3, color=None):
        if (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x) == 0:
            raise ValueError('Points must not be on the same line')
        super().__init__(p1, p2, p3, color)


class IsoscelesTriangle(Triangle):
    def __init__(self, p1, p2, l, color=None):
        d = abs(Line(p1, p2))
        if l < d:
            raise ValueError('Side length must be bigger than base length')
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
        super().__init__(p1, p2, p3, color)


class Rectangle(Polygon):
    def __init__(self, l_d, r_u, color=None):
        l_u = Point(l_d.x, r_u.y)
        r_d = Point(r_u.x, l_d.x)
        super().__init__(l_d, l_u, r_d, r_u, color)


class Square(Rectangle):
    def __init__(self, p, l, color=None):
        l_d = p
        r_u = Point(p.x + l, p.y + l)
        super().__init__(l_d, r_u, color)


class EquilateralPolygon(Polygon):
    def __init__(self, center_point, r, vertices, color=None):
        self.r = round(r)
        if r <= 0:
            raise ValueError('Radius must be 1 or higher')
        if vertices < 3:
            raise ValueError('Polygon must have 3 or more vertices')
        points = []
        angles = 360 / vertices
        for n in range(vertices):
            angle = angles * n
            points.append(Point(center_point.x + math.cos(math.radians(angle)) * r,
                                center_point.y + math.sin(math.radians(angle)) * r))
        super().__init__(*points, color)
