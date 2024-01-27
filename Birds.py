from pygame.sprite import Sprite
from Groups import all_sprites, enemies
from utils import load_image


class Bird(Sprite):
    bird_fly_0 = load_image("bird_0.png")
    bird_fly_1 = load_image("bird_1.png")
    bird_fly_2 = load_image("bird_2.png")
    reset_frame = 3

    def __init__(self, spawn, speed=35):
        super().__init__(all_sprites, enemies)
        self.image = Bird.bird_fly_0
        self.rect = self.image.get_rect()
        self.rect.y = 150
        self.status_down = None
        self.frame = 0
        self.reset_frame = Bird.reset_frame
        self.rect.bottom = 735
        self.rect.x = spawn
        self.movement = [-1 * speed, 0]

    def update(self):
        self.frame += 1
        self.rect = self.rect.move(self.movement)
        if self.rect.right < 0:
            self.kill()
        if self.frame == self.reset_frame:
            self.frame = 0
            if self.image == Bird.bird_fly_0:
                self.image = Bird.bird_fly_1
            elif self.image == Bird.bird_fly_1:
                self.image = Bird.bird_fly_2
            elif self.image == Bird.bird_fly_2:
                self.image = Bird.bird_fly_0
