import pygame

from utils import screen


class Background:  # класс фона
    background_back_first = pygame.image.load("DINO_IMAGES/fone_0.png").convert_alpha()  # загружаем картинки
    background_back_second = pygame.image.load("DINO_IMAGES/fone_1.png").convert_alpha()
    background_back_third = pygame.image.load("DINO_IMAGES/fone_2.png").convert_alpha()
    background_front = pygame.image.load("DINO_IMAGES/fone_3.png").convert_alpha()

    def __init__(self):  # инициализация
        super().__init__()
        self.background_back_first = Background.background_back_first  # пишем в переменные
        self.background_back_second = Background.background_back_second
        self.background_back_third = Background.background_back_third
        self.background_front = Background.background_front
        self.background_back_first_speed = 0  # координаты картинок при сдвиге
        self.background_back_second_speed = 0
        self.background_back_third_speed = 0
        self.background_front_speed = 0
        self.background_back_first_shift = 0.4  # скорость сдвига слоёв фона
        self.background_back_second_shift = 1
        self.background_back_third_shift = 1.7
        self.background_front_shift = 3.5
        self.shift_factor = 3  # множитель скорости
        self.width = 1920  # ширина окна

    def update(self, shift=-1, multiply_shift=1, width=-1, background_back_first_shift=-1,  # метод обновления экрана
               background_back_second_shift=-1, background_back_third_shift=-1, background_front_shift=-1):
        # # # # # # # # # # # # # # # # # # # # # # #/ Конфигурация при необходимости /# # # # # # # # # # # # # # # # #
        if width != -1:
            self.width = width
        if background_back_first_shift != -1:
            self.background_back_first_shift = background_back_first_shift
        if background_back_second_shift != -1:
            self.background_back_second_shift = background_back_second_shift
        if background_back_third_shift != -1:
            self.background_back_third_shift = background_back_third_shift
        if background_front_shift != -1:
            self.background_front_shift = background_front_shift
        if shift != -1:
            self.shift_factor = shift
        # # # # # # # # # # # # # # # # # # # # # # # # #/ Отрисовка слоёв фона /# # # # # # # # # # # # # # # # # # # #
        self.shift_factor = self.shift_factor * multiply_shift
        rel_background_back_first_speed = self.background_back_first_speed % self.background_back_first.get_rect().width
        screen.blit(self.background_back_first,
                    (rel_background_back_first_speed - self.background_back_first.get_rect().width, 0))
        if rel_background_back_first_speed < self.width:
            screen.blit(self.background_back_first, (rel_background_back_first_speed, 0))
        self.background_back_first_speed -= self.background_back_first_shift * self.shift_factor

        rel_background_back_second_speed = \
            self.background_back_second_speed % self.background_back_second.get_rect().width
        screen.blit(self.background_back_second,
                    (rel_background_back_second_speed - self.background_back_second.get_rect().width, 0))
        if rel_background_back_second_speed < self.width:
            screen.blit(self.background_back_second, (rel_background_back_second_speed, 0))
        self.background_back_second_speed -= self.background_back_second_shift * self.shift_factor

        rel_background_back_third_speed = self.background_back_third_speed % self.background_back_third.get_rect().width
        screen.blit(self.background_back_third,
                    (rel_background_back_third_speed - self.background_back_third.get_rect().width, 0))
        if rel_background_back_third_speed < self.width:
            screen.blit(self.background_back_third, (rel_background_back_third_speed, 0))
        self.background_back_third_speed -= self.background_back_third_shift * self.shift_factor

        rel_background_front_speed = self.background_front_speed % self.background_front.get_rect().width
        screen.blit(self.background_front, (rel_background_front_speed - self.background_front.get_rect().width, 0))
        if rel_background_front_speed < self.width:
            screen.blit(self.background_front, (rel_background_front_speed, 0))
        self.background_front_speed -= self.background_front_shift * self.shift_factor
        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
