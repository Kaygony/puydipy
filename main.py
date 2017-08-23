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
    ch = character.Snake(3)
    p = figures.Point(100, 100)
    left = False
    right = False
    up = False
    down = False
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.fill(colors.WHITE)
        figures.Square(p, 20)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ch.move_left()
            elif event.key == pygame.K_RIGHT:
                ch.move_right()
            elif event.key == pygame.K_UP:
                ch.move_up()
            elif event.key == pygame.K_DOWN:
                ch.move_down()
            if event.key == pygame.K_ESCAPE:
                game_exit = True

        ch.update()
        ch.draw(game_display)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()

