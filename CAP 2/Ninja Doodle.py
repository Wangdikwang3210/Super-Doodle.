# Ninja Doodle Game
import random

import pygame
from pygame import mixer

pygame.init()

# Library Game Content:
White = (255, 255, 255)
Black = (0, 0, 0)
Gray = (128, 128, 128)
Width = 400
Height = 500
background = White
player = pygame.transform.scale(pygame.image.load('Doodle.png'), (90, 70))
fps = 60
font = pygame.font.Font('freesansbold.ttf', 16)
timer = pygame.time.Clock()
score = 0
high_score = 0
Game_over = False

# Game variables
player_x = 170
player_y = 400
platforms = [[170, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [170, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
jump = False
y_change = 0
x_change = 0
player_speed = 3
score_last = 0
Ninja_Spring  = 2
jump_last = 0

# Create Screen
screen = pygame.display.set_mode([Width, Height])
pygame.display.set_caption('Ninja Doodle')

# Background music
mixer.music.load('Phudo_Sa_lyrics_video___%40SonamWangchen___%40YeshiLhendupFilms___%40_eyeball____Lyrical_Video(256k).mp3')
mixer.music.play(-1)

# Function to check for collisions with blocks (obstacles)
def check_collisions(rect_list, j):
    global player_x
    global player_y
    global y_change
    for i in range(len(rect_list)):
        if rect_list[i].colliderect([player_x + 20, player_y + 60, 35, 5]) and y_change >= 0:
            # Change y_change to enable the jump
            y_change = -10  # Adjust this value to control the jump height
            j = True
    return j

# update player y position every loop
def update_player(y_pos):
    global y_change
    jump_height = 12 # The height of jump of the Character
    gravity = 0.4  # Adjust the gravity value to control falling speed
    y_pos += y_change
    y_change += gravity
    return y_pos


# handle movement of platforms as game progresses:
def update_platforms(my_list, y_pos, change):
    global score
    if y_pos < 250 and change < 0:
        for i in range(len(my_list)):
            my_list[i][1] -= change
    else:
        pass
    for item in range(len(my_list)):
        if my_list[item][1] > 500:
            my_list[item] = [random.randint(10, 320), random.randint(-50, -10), 70, 10] 
            score += 1
    return my_list
            

running = True
while running:
    timer.tick(fps)
    screen.fill(background)
    screen.blit(player, (player_x, player_y))
    blocks = []
    score_text = font.render('H-SCORE: '+ str(score), True, Gray, background)
    screen.blit(score_text, (5, 10))
    high_score_text = font.render('SCORE: '+ str(score), True, Gray, background)
    screen.blit(high_score_text, (15, 35))
    
    score_text = font.render('N-SPRING: '+ str(Ninja_Spring), True, Gray, background)
    screen.blit(score_text, (280, 0))
    if Game_over:
        Game_over_text = font.render('GAME OVER: Spacebar to RESTART!', True, Gray, background)
        screen.blit(Game_over_text, (80, 80))

 
    for i in range(len(platforms)):
        block = pygame.draw.rect(screen, Gray, platforms[i], 0, 4)
        blocks.append(block)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Game_over:
                Game_over = False
                score = 0
                player_x = 170
                player_y = 400
                background = White
                score_last = 0
                Ninja_Spring = 2
                jump_last = 0
                platforms = [[170, 480, 70, 10], [85, 370, 70, 10], [265, 370, 70, 10], [170, 260, 70, 10], [85, 150, 70, 10], [265, 150, 70, 10], [175, 40, 70, 10]]
            if event.key == pygame.K_SPACE and not Game_over and Ninja_Spring > 0:
                Ninja_Spring -= 1
                y_change = -15
            if event.key == pygame.K_LEFT:
                x_change = -player_speed
            if event.key == pygame.K_RIGHT:
                x_change = player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                x_change = 0
            if event.key == pygame.K_d:
                x_change = 0


    jump = check_collisions(blocks, jump)
    player_x += x_change

    if player_y < 440:
        player_y = update_player(player_y)
    else:
        Game_over = True
        y_change = 0

    platforms = update_platforms(platforms, player_y, y_change)

    if player_x < -20:
        player_x = -20
    elif player_x > 330:
        player_x = 330

    if x_change > 0:
        player = pygame.transform.scale(pygame.image.load('Doodle.png'), (90, 70))
    elif x_change < 0:
        player = pygame.transform.flip(pygame.transform.scale(pygame.image.load('Doodle.png'), (90, 70)), 1, 0)

    if score > high_score:
        high_score = score

    if  score - score_last > 15:
        score_last = score
        background = (random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))

    if score - jump_last > 50:
        jump_last = score
        Ninja_Spring += 1

    pygame.display.flip()

pygame.quit()