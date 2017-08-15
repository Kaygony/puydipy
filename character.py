import math

import pygame

import figures


class Character(figures.Drawable):
    def __init__(self, x, y):
        self.body_parts = {'head': figures.Circle(x, y - 5 * 2, 5 * 2),
                           'torso': figures.Line(figures.Point(x, y), figures.Point(x, y + 25 * 2)),
                           'l_arm': figures.Line(figures.Point(x, y), figures.Point(x - 10 * 2, y + 15 * 2)),
                           'r_arm': figures.Line(figures.Point(x, y), figures.Point(x + 10 * 2, y + 15 * 2)),
                           'l_leg': figures.Line(figures.Point(x, y + 25 * 2), figures.Point(x - 10 * 2, y + 45 * 2)),
                           'r_leg': figures.Line(figures.Point(x, y + 25 * 2), figures.Point(x + 10 * 2, y + 45 * 2))}

    def draw(self, game_display):
        for body_part in self.body_parts.values():
            body_part.draw(game_display)

    def wave_arms(self, game_display):
        while (self.body_parts['l_arm'].start.y / self.body_parts['l_arm'].start.x) != (2 * math.pi) / 3:
            self.body_parts['l_arm'].end.x += -1
            self.body_parts['l_arm'].end.y += -1
            self.body_parts['r_arm'].end.x += 1
            self.body_parts['r_arm'].end.y += -1
            self.draw(game_display)
            pygame.display.update()
        while (self.body_parts['l_arm'].start.y / self.body_parts['l_arm'].start.x) != (4 * math.pi) / 3:
            self.body_parts['l_arm'].end.x += 1
            self.body_parts['l_arm'].end.y += 1
            self.body_parts['r_arm'].end.x += -1
            self.body_parts['r_arm'].end.y += 1
            self.draw(game_display)
            pygame.display.update()

    def move(self):
        pass
