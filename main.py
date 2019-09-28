import random

import pygame

import character
import colors
import figures
import game
import peewee_bd

pygame.init()

display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('MyGame')
clock = pygame.time.Clock()
peewee_bd.Snake.create_table(fail_silently=True)


def game_loop():
    ch = character.Snake(3)
    apple = character.Apple(1, 1)
    game_exit = False
    peewee_bd.Snake.get_or_create(name='Snake')
    snake = peewee_bd.Snake.get(name='Snake')
    ch.score = snake.score
    ch.direction = snake.direction
    ch.segment[0] = snake.head_coords
    for i in range(ch.length - 1, 0, -1):
        ch.segment[i] = snake.body_coords[i - 1]

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
                snake.score = ch.score
                snake.head_coords = ch.segment[0]
                for i in range(ch.length - 1, 0, -1):
                    snake.body_coords.append(figures.Point(ch.segment[i - 1].x, ch.segment[i - 1].y))
                snake.direction = ch.direction
                game_exit = True

        ch.update()
        ch.draw(game_display)
        apple.draw(game_display)

        for i in range(1, ch.length):
            if game.collision(ch.segment[i], ch.segment[0], 15):
                print("You lose!")
                snake.score = 0
                snake.head_coords = (0, 0)
                for i in range(ch.length - 1, 0, -1):
                    snake.body_coords[i] = (0, 0)
                snake.direction = 0
                exit(0)

        for i in range(0, ch.length):
            if game.collision(ch.segment[0], apple, 15):
                apple.x = random.randint(1, 40) * 20
                apple.y = random.randint(1, 30) * 20
                ch.score += 1
                print(ch.score)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
