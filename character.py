import figures


class Character(figures.Figure):
    def __init__(self, x, y, color=None):
        self.body = (figures.Line(figures.Point(x, y), figures.Point(x, y + 100), color),
                     figures.Circle(x, y - 25, 25, color),
                     figures.Line(figures.Point(x, y), figures.Point(x - 50, y + 75), color),
                     figures.Line(figures.Point(x, y), figures.Point(x + 50, y + 75), color),
                     figures.Line(figures.Point(x, y + 100), figures.Point(x - 50, y + 150), color),
                     figures.Line(figures.Point(x, y + 100), figures.Point(x + 50, y + 150), color))
        super().__init__(color)

    def draw(self, game_display):
        for body_part in self.body:
            body_part.draw(game_display)


''' думал над этим(не работает хех , но хочу пока оставить)
class Body(Character):
    def __init__(self, x, y):
        self.torso = figures.Line(figures.Point(x, y), figures.Point(x, y + 100))
        self.head = figures.Circle(x, y-25, 25)
        self.left_hand = figures.Line(figures.Point(x, y), figures.Point(x - 50, y + 75))
        self.right_hand = figures.Line(figures.Point(x, y), figures.Point(x + 50, y + 75))
        self.left_lag = figures.Line(figures.Point(x, y + 100), figures.Point(x - 50, y + 150))
        self.right_lag = figures.Line(figures.Point(x, y + 100), figures.Point(x + 50, y + 150))
        self.body = (self.torso, self.head, self.left_hand, self.right_hand,
                     self.left_lag, self.right_lag)'''
