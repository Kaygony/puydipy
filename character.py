import time

import pygame

import colors
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
        l_arm_up = self.body_parts['l_arm'].start.y
        l_arm_down = self.body_parts['l_arm'].end.y
        while self.body_parts['l_arm'].end.y != l_arm_up:
            self.body_parts['l_arm'].color = colors.WHITE
            self.body_parts['r_arm'].color = colors.WHITE
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            self.body_parts['l_arm'].color = colors.BLACK
            self.body_parts['r_arm'].color = colors.BLACK
            self.body_parts['l_arm'].end.y += -1
            self.body_parts['l_arm'].end.x += -0.314
            self.body_parts['r_arm'].end.y += -1
            self.body_parts['r_arm'].end.x += 0.314
            print(self.body_parts['l_arm'].end)
            print(self.body_parts['r_arm'].end)
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            pygame.display.update()
            time.sleep(0.05)
        while self.body_parts['l_arm'].end.y != l_arm_down:
            self.body_parts['l_arm'].color = colors.WHITE
            self.body_parts['r_arm'].color = colors.WHITE
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            self.body_parts['l_arm'].color = colors.BLACK
            self.body_parts['r_arm'].color = colors.BLACK
            self.body_parts['l_arm'].end.y += 1
            self.body_parts['l_arm'].end.x += 0.314
            self.body_parts['r_arm'].end.y += 1
            self.body_parts['r_arm'].end.x += -0.314
            self.body_parts['l_arm'].draw(game_display)
            self.body_parts['r_arm'].draw(game_display)
            pygame.display.update()
            time.sleep(0.05)

    def mov(self):
        pass
