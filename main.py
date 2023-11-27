import pygame
import time
import random

#init pygame
pygame.init()

#define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)

width , height = 600, 400

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sarbarth Snake Game")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score):
    text = score_font.render("Score:" + str(score), True, orange)
    game_display.blit(text, [0,0])

def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [pixel[0], pixel[1], snake_size, snake_size])

def run_game():

    game_over = False
    game_close = False

    X = width/4
    Y = width/4

    X_speed = 0
    Y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_X  = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
    target_Y = round(random.randrange(0, height-snake_size)/10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(black)
            game_over_message = message_font.render("Damn!! You lost Ugly Bitch", True, red)
            game_display.blit(game_over_message, [width/4, height/4])
            print_score(snake_length-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_2:
                            run_game()
                if event.type == pygame.QUIT:
                            game_over = True
                            game_close = False    



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X_speed = -snake_size
                    Y_speed = 0
                if event.key == pygame.K_UP:
                    X_speed = 0
                    Y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    X_speed = 0
                    Y_speed = snake_size 
                if event.key == pygame.K_RIGHT:
                    X_speed = snake_size
                    Y_speed = 0     
        if X >= width or X < 0 or Y >=height or Y < 0:
            game_close = True

        X += X_speed
        Y += Y_speed   

        game_display.fill(black)
        pygame.draw.rect(game_display, orange,[target_X, target_Y, snake_size, snake_size])

        snake_pixels.append([X,Y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[:-1]:
            if pixel == [X,Y]:
              game_close = True

        draw_snake(snake_size, snake_pixels)
        print_score(snake_length-1)

        pygame.display.update()

        if X == target_X and Y == target_Y:
            target_X  = round(random.randrange(0, width-snake_size) / 10.0) * 10.0
            target_Y = round(random.randrange(0, height-snake_size) / 10.0) * 10.0 
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

run_game()                                           