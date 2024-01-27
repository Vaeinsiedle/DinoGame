import pygame
from pygame.sprite import Sprite

from Groups import all_sprites
from utils import load_image


class Ground(Sprite):
    speed = 25
    def __init__(self):
        super().__init__(all_sprites)
        self.image = load_image('Land.png')
        self.rect = self.image.get_rect()
        self.rect.y = 850


    def update(self):
        head = self.image.subsurface((0, 0, self.speed, self.rect.height))
        tail = self.image.subsurface((self.speed, 0, self.rect.width - self.speed, self.rect.height))
        new_land = pygame.Surface(self.rect.size, pygame.SRCALPHA, 32)
        new_land.blit(tail, (0, 0))
        new_land.blit(head, (self.rect.width - self.speed, 0))
        self.image = new_land