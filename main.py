import pygame

import character
import colors
import figures

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MyGame')
clock = pygame.time.Clock()

def game_loop():
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.fill(colors.WHITE)

        p1 = figures.Point(150, 160)
        p2 = figures.Point(200, 200)
        p1.draw(game_display)
        figures.Line(p1, p2, color=colors.RED).draw(game_display)
        p2.draw(game_display)
        figures.Triangle(figures.Point(350, 400), figures.Point(300, 200), figures.Point(400, 350)).draw(game_display)
        character.Character(500, 500, colors.BLACK).draw(game_display)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()