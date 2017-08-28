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
peewee_bd.db.connect()
peewee_bd.db.create_tables(peewee_bd.Snake)


def game_loop():
    ch = character.Snake(3)
    apple = character.Apple(1, 1)
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        peewee_bd.Snake.get_or_create(name='Snake')

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
                peewee_bd.Snake.create(name='Snake', score=ch.score,
                                       head_coords=(ch.segment_x[0], ch.segment_y[0]),
                                       teil_coords=(ch.segment_x[ch.length], ch.segment_y[ch.length]),
                                       direction=ch.direction)
                peewee_bd.db.close()
                game_exit = True

        ch.update()
        ch.draw(game_display)
        apple.draw(game_display)

        figures.Circle(200, 200, 20, colors.RED).draw(game_display)

        for i in range(1, ch.length):
            if game.collision(ch.segment_x[i], ch.segment_y[i], ch.segment_x[0], ch.segment_y[0], 15):
                print("You lose!")
                peewee_bd.Snake.create(name='Snake', score=0,
                                       head_coords=(0, 0),
                                       teil_coords=(0, 0),
                                       direction=0)
                peewee_bd.db.close()
                exit(0)

        for i in range(0, ch.length):
            if game.collision(ch.segment_x[0], ch.segment_y[0], apple.x, apple.y, 15):
                apple.x = random.randint(1, 40) * 20
                apple.y = random.randint(1, 30) * 20
                ch.score += 1
                print(ch.score)

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
