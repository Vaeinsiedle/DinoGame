import pygame

from Groups import all_sprites, enemies

from utils import load_image


class Tumbleweed(pygame.sprite.Sprite):
    tumbleweed_image = load_image("Tumbleweed_1.png")
    def __init__(self, spawn, speed=35):
        super().__init__(all_sprites, enemies)
        self.image = Tumbleweed.tumbleweed_image
        self.rect = self.image.get_rect()
        self.orig_image = self.image
        self.rect.bottom = 855
        self.rect.x = spawn
        self.angle = 0
        self.movement = [-1 * speed, 0]

    def update(self):
        self.angle += 15
        self.rotate()
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()

    def rotate(self):
        self.image = pygame.transform.rotozoom(self.orig_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)