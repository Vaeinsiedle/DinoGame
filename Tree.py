import pygame
import random
from Groups import all_sprites, trees
from utils import load_image


class Tree(pygame.sprite.Sprite):
    images = [load_image(f'Tree_{i}.png') for i in range(5)]

    def __init__(self, speed=15):
        super().__init__(all_sprites, trees)
        self.image = random.choice(self.images)
        self.rect = self.image.get_rect()
        self.rect.bottom = 850
        self.rect.x = 1920
        self.movement = [-1*speed, 0]

    def update(self):
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()
