import pygame
import random

from Groups import all_sprites, enemies

from utils import load_image


class Cactus(pygame.sprite.Sprite):
    images = [load_image(f'cactus_{i}.png') for i in range(11)]
    def __init__(self, speed=25):
        super().__init__(all_sprites, enemies)
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.bottom = 855
        self.rect.x = 1920
        self.movement = [-1*speed, 0]


    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()
