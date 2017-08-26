import random

import pygame

import character
import colors
import figures
import game

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('MyGame')
clock = pygame.time.Clock()

def game_loop():
    ch = character.Snake(3)
    apple = character.Apple(1, 1)
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        game_display.fill(colors.WHITE)

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
        apple.draw(game_display)

        figures.Circle(200, 200, 20, colors.RED).draw(game_display)

        for i in range(2, ch.length):
            if game.collision(ch.segment_x[0], ch.segment_y[0], ch.segment_x[i], ch.segment_y[i], 10):
                print("You lose!")
                exit(0)

        for i in range(0, ch.length):
            if game.collision(apple.x, apple.y, ch.segment_x[0], ch.segment_y[0], 10):
                apple.x = random.randint(2, 9) * 10
                apple.y = random.randint(2, 9) * 10
                ch.score += 1
                print(ch.score)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
