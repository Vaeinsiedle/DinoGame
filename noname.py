import pygame
from pygame.locals import *
import sys


def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


# define display surface
W, H = 1920, 1080
HW, HH = W / 2, H / 2
AREA = W * H



# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Типо фон")
FPS = 60

bkgd = pygame.image.load("DINO_IMAGES/fone_0.png").convert_alpha()
bkgdd = pygame.image.load("DINO_IMAGES/fone_1.png").convert_alpha()
bkgddd = pygame.image.load("DINO_IMAGES/fone_2.png").convert_alpha()
bkgdddd = pygame.image.load("DINO_IMAGES/fone_3.png").convert_alpha()

x = 0
xx = 0
xxx = 0
xxxx = 0
a = 2
# main loop
while True:
    events()

    rel_x = x % bkgd.get_rect().width
    DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    if rel_x < W:
        DS.blit(bkgd, (rel_x, 0))
    x -= 0.4 * a

    rel_xx = xx % bkgdd.get_rect().width
    DS.blit(bkgdd, (rel_xx - bkgdd.get_rect().width, 0))
    if rel_xx < W:
        DS.blit(bkgdd, (rel_xx, 0))
    xx -= 1 * a

    rel_xxx = xxx % bkgddd.get_rect().width
    DS.blit(bkgddd, (rel_xxx - bkgddd.get_rect().width, 0))
    if rel_xxx < W:
        DS.blit(bkgddd, (rel_xxx, 0))
    xxx -= 1.7 * a

    rel_xxxx = xxxx % bkgdddd.get_rect().width
    DS.blit(bkgdddd, (rel_xxxx - bkgdddd.get_rect().width, 0))
    if rel_xxxx < W:
        DS.blit(bkgdddd, (rel_xxxx, 0))
    xxxx -= 3.5 * a
    a += 0.001
    pygame.display.flip()
    CLOCK.tick(FPS)