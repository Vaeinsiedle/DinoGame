import os
import random

import pygame

import Scoreboard
from Background import Background
from Birds import Bird
from Ground import Ground
from Groups import trees, all_sprites, enemies
from Speed import Speed
from utils import load_image

pygame.init()
fps = 16
size = width, height = 1920, 1080
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
retbutton_image = load_image('replay_button.png')
gameover_image = load_image('game_over.png')
font = pygame.font.Font(None, 30)
jump_sound = pygame.mixer.Sound('Sound/Dino_jump.wav')
die_sound = pygame.mixer.Sound('Sound/Dino_die.wav')
checkPoint_sound = pygame.mixer.Sound('Sound/Dino_checkPoint.wav')

from Dino import Dino
from Cactus import Cactus
from Tumbleweed import Tumbleweed
from Generation import Generation
from Tree import Tree


def disp_gameOver_msg(retbutton_image, gameover_image):
    retbutton_rect = retbutton_image.get_rect()
    retbutton_rect.centerx = width / 2.75
    retbutton_rect.top = height*0.35

    gameover_rect = gameover_image.get_rect()
    gameover_rect.centerx = width / 2.75
    gameover_rect.centery = height*0.25

    screen.blit(retbutton_image, retbutton_rect)
    screen.blit(gameover_image, gameover_rect)

def restart():
    game_pause = True
    while game_pause:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_pause = False
    kill_enemies()

def kill_enemies():
    for i in enemies:
        i.kill()
    for j in trees:
        j.kill()


def main():
    running = True
    background = Background()
    scoreboard = Scoreboard.ScoreBoard()
    dino = Dino()
    ground = Ground()
    generate = Generation()
    count = 0
    number = random.randrange(30, 60)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scoreboard.save_score()
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    scoreboard.save_score()
                    running = False
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                dino.jump()
                if pygame.mixer.get_init() != None:
                    jump_sound.play()
            if key[pygame.K_DOWN]:
                dino.down()
        if scoreboard.get_score() > 1 and scoreboard.get_score() % 500 == 0:
            if pygame.mixer.get_init() != None:
                checkPoint_sound.play()
        if pygame.sprite.spritecollide(dino, enemies, False):
            screen.fill(pygame.Color("white"))
            background.update()
            dino.death()
            disp_gameOver_msg(retbutton_image, gameover_image)
            scoreboard.print_score()
            all_sprites.draw(screen)
            pygame.display.flip()
            if pygame.mixer.get_init() != None:
                die_sound.play()
            restart()
            scoreboard.save_score()
            scoreboard = Scoreboard.ScoreBoard()
        else:
            screen.fill(pygame.Color("white"))
            background.update()
            scoreboard.print_score()
            d = generate.generate(40, 1920)
            if d[0] != -1:
                if d[0] == 0:
                    Cactus()
                if d[0] == 1:
                    if scoreboard.get_score() > 750:
                        Bird(spawn=d[1])
                    else:
                        Cactus()
                if d[0] == 2:
                    Tumbleweed(spawn=d[1])
                if d[0] == 3:
                    Tree()
            all_sprites.draw(screen)
            all_sprites.update()
            scoreboard.print_score()
            pygame.display.flip()
            clock.tick(fps)
            count += 1

    pygame.quit()


main()
