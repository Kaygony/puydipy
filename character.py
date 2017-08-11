import figures


class Character:
    def __init__(self, x, y):
        self.body_parts = {'head': figures.Circle(x, y - 5, 5),
                           'torso': figures.Line(figures.Point(x, y), figures.Point(x, y + 25)),
                           'l_arm': figures.Line(figures.Point(x, y), figures.Point(x - 10, y + 15)),
                           'r_arm': figures.Line(figures.Point(x, y), figures.Point(x + 10, y + 15)),
                           'l_leg': figures.Line(figures.Point(x, y + 25), figures.Point(x - 10, y + 20)),
                           'r_leg': figures.Line(figures.Point(x, y + 25), figures.Point(x + 10, y + 200))}

    def draw(self, game_display):
        for body_part in self.body_parts.values():
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
