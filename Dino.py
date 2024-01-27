import pygame
import os

from pygame.sprite import Sprite

from Groups import all_sprites
from utils import load_image


class Dino(Sprite):
    gravity = 4.35
    dino_image_stand = load_image("dino_stand.png")
    dino_image_run_first = load_image("dino_0.png")
    dino_image_run_second = load_image("dino_1.png")
    dino_image_down_first = load_image("dino_down_0.png")
    dino_image_down_second = load_image("dino_down_1.png")
    dino_image_shock = load_image("dino_shock.png")
    reset_frame = 2

    def __init__(self, dy=15, dx=5):
        super().__init__(all_sprites)
        self.image = Dino.dino_image_stand
        self.rect = self.image.get_rect()
        self.rect.y = 715
        self.velocity_dino = [dy, dx]
        self.gravity = Dino.gravity
        self.status_down = None
        self.status_jump = None
        self.status_death = None
        self.frame = 0
        self.reset_frame = Dino.reset_frame


    def jump(self):
        if self.rect.y == 715:
            self.status_jump = True
            self.image = Dino.dino_image_stand
            self.velocity_dino[0] = 50

    def down(self):
        self.status_down = True
        self.image = Dino.dino_image_down_first

    def death(self):
        if self.status_down:
            self.rect.y = 715
        self.image = Dino.dino_image_shock
        self.status_death = True


    def update(self):
        self.frame += 1
        if self.status_death:
            pass

        if self.status_jump:
            self.image = Dino.dino_image_stand
            self.velocity_dino[0] -= self.gravity
            self.rect.y -= self.velocity_dino[0]
            if self.rect.y > 715:
                self.status_jump = False
                self.rect.y = 715

        elif self.frame > self.reset_frame:
            self.frame = 0

            if self.status_down:
                self.rect.y = 760
                if self.image == Dino.dino_image_down_first:
                    self.image = Dino.dino_image_down_second
                else:
                    self.image = Dino.dino_image_down_first
                if not pygame.key.get_pressed()[pygame.K_DOWN]:
                    self.status_down = False
            else:
                self.rect.y = 715
                if self.image == Dino.dino_image_run_first:
                    self.image = Dino.dino_image_run_second
                else:
                    self.image = Dino.dino_image_run_first




