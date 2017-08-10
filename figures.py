import math

import pygame

from colors import *


class Figure:
    def __init__(self, color=None):
        if not color:
            color = BLACK
        self.color = color

    def draw(self, game_display):
        raise NotImplementedError


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

    def draw(self, game_display):
        pygame.draw.circle(game_display, self.color, self.coords, 1)


class Circle(Point):
    def __init__(self, x, y, r, color=None):
        super().__init__(x, y, color)
        self.r = round(r)

    def draw(self, game_display):
        pygame.draw.circle(game_display, self.color, self.coords, self.r)


class Polygon(Figure):
    def __init__(self, *points, color=None):
        self.points = points
        super().__init__(color)

    def __repr__(self):
        return '<{0}{1} figure>'.format(self.__class__.__name__, self.points)

    def draw(self, game_display):
        pygame.draw.polygon(game_display, self.color, [self.points[i].coords for i in range(len(self.points)-1)])


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

    def draw(self, game_display):
        pygame.draw.line(game_display, self.color, self.start.coords, self.end.coords)


class Triangle(Polygon):
    def __init__(self, p1, p2, p3, color=None):
        super().__init__(p1, p2, p3, color)


class IsoscelesTriangle(Triangle):
    def __init__(self, p1, p2, l, color=None):
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
        points = []
        angles = 360 / vertices
        for n in range(vertices):
            angle = angles * n
            points.append(Point(center_point.x + math.cos(math.radians(angle)) * r,
                                center_point.y + math.sin(math.radians(angle)) * r))
        super().__init__(*points, color)
