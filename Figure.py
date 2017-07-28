class Figure(object):
    pass

class Point(Figure):
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Circle(Point):
        def __init__(self,x,y,r):
            Point.__init__(self,x,y)
            self.r=r

class CTriangle(Circle):
           def __init__(self,x,y,r):
               Circle.__init__(self,x,y,r)
               #не понял че тут к чему



class Polygon(Figure):
    def __init__(self,*points):
        self.points=points
#не уверен что дальше делал правильно
class Line(Polygon):
        def __init__(self,p1,p2):
            self.p1=p1
            self.p2=p2

class Triangle(Polygon):
    def __init__(self,p1,p2,p3):
        self.p1=p1
        self.p2=p2
        self.p3=p3

class IsoscelesTriangle(Triangle):    #равнобедренный треугольник(буду делать через окружности и нахождение точки пересечения. формулу вывел ,в код перевести не успел)
    def __init__(self,p1,p2,l):
        self.p1=p1
        self.p2=p2
        self.l=l


#дальше пока не делал
class Rectangle(Polygon):



