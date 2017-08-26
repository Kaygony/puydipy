import random

import colors
import figures

MOVE_SPEED = 2


class Character(figures.Drawable):
    def __init__(self, x, y):
        self.body_parts = {'head': figures.Circle(x, y - 10, 10),
                           'torso': figures.Line(figures.Point(x, y), figures.Point(x, y + 50)),
                           'l_arm': figures.Line(figures.Point(x, y), figures.Point(x - 20, y + 40)),
                           'r_arm': figures.Line(figures.Point(x, y), figures.Point(x + 20, y + 40)),
                           'l_leg': figures.Line(figures.Point(x, y + 50), figures.Point(x - 20, y + 90)),
                           'r_leg': figures.Line(figures.Point(x, y + 50), figures.Point(x + 20, y + 90))}
        self.trigger_up = 0
        self.x_move = 0

    def draw(self, game_display):
        for body_part in self.body_parts.values():
            body_part.draw(game_display)

    def wave_arms(self, game_display):
        if self.body_parts['l_arm'].end.y == self.body_parts['head'].y - 15:
            self.trigger_up = 1
        if self.body_parts['l_arm'].end.y == self.body_parts['torso'].end.y - 5:
            self.trigger_up = 0
        if self.trigger_up == 0:
            self.body_parts['l_arm'].end.x += -0.314
            self.body_parts['l_arm'].end.y += -1
            self.body_parts['r_arm'].end.x += 0.314
            self.body_parts['r_arm'].end.y += -1
            self.draw(game_display)
        if self.trigger_up == 1:
            self.body_parts['l_arm'].end.x += 0.314
            self.body_parts['l_arm'].end.y += 1
            self.body_parts['r_arm'].end.x += -0.314
            self.body_parts['r_arm'].end.y += 1
            self.draw(game_display)

    def move(self, left, right):
        if left:
            self.x_move = -MOVE_SPEED

        if right:
            self.x_move = MOVE_SPEED

        if not (left or right):
            self.x_move = 0

        self.body_parts['head'].x += self.x_move
        self.body_parts['torso'].start.x += self.x_move
        self.body_parts['torso'].end.x += self.x_move
        self.body_parts['l_arm'].start.x += self.x_move
        self.body_parts['l_arm'].end.x += self.x_move
        self.body_parts['r_arm'].start.x += self.x_move
        self.body_parts['r_arm'].end.x += self.x_move
        self.body_parts['l_leg'].start.x += self.x_move
        self.body_parts['l_leg'].end.x += self.x_move
        self.body_parts['r_leg'].start.x += self.x_move
        self.body_parts['r_leg'].end.x += self.x_move


class Apple(figures.Drawable):
    def __init__(self, x, y):
        self.x = x * random.randint(0, 780)
        self.y = y * random.randint(20, 580)

    def draw(self, game_display):
        figures.Square(figures.Point(self.x, self.y), 20, color=colors.RED).draw(game_display)


class Snake(figures.Drawable):
    step = 20
    direction = 1
    score = 0

    # Для ограничения скорости
    update_count_max = 8
    update_count = 0

    def __init__(self, length):
        self.length = length + self.score
        self.segment_x = []
        self.segment_y = []
        for i in range(0, length):
            self.segment_x.append(340 + i * self.step)
            self.segment_y.append(280)

    def update(self):

        self.update_count = self.update_count + 1
        if self.update_count > self.update_count_max:

            for i in range(self.length - 1, 0, -1):
                self.segment_x[i] = self.segment_x[i - 1]
                self.segment_y[i] = self.segment_y[i - 1]

            if self.direction == 0:
                self.segment_x[0] = self.segment_x[0] + self.step
            if self.direction == 1:
                self.segment_x[0] = self.segment_x[0] - self.step
            if self.direction == 2:
                self.segment_y[0] = self.segment_y[0] - self.step
            if self.direction == 3:
                self.segment_y[0] = self.segment_y[0] + self.step

            self.update_count = 0

    def move_right(self):
        if self.direction != 1:
            self.direction = 0

    def move_left(self):
        if self.direction != 0:
            self.direction = 1

    def move_up(self):
        if self.direction != 3:
            self.direction = 2

    def move_down(self):
        if self.direction != 2:
            self.direction = 3

    def draw(self, game_display):
        for i in range(0, self.length):
            figures.Square(figures.Point(self.segment_x[i], self.segment_y[i]), 20).draw(game_display)
