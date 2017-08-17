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
    ch = character.Character(400, 400)
    left = False
    right = False
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
        ch.wave_arms(game_display)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_LEFT:
                left = False
        ch.move(left, right)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()

