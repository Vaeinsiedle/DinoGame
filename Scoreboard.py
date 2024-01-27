import pygame
import cryptocode

from Groups import all_sprites
from utils import screen


class ScoreBoard:  # класс фона
    key = "49682-85521-10923-15450-12851-94143-01257-54571-00348"  # ключ
    font_name = pygame.font.match_font('arial black')  # поиск шрифта

    def __init__(self):  # инициализация
        super().__init__()
        self.score = 0  # текущий счёт ноль
        file = open("score.txt", "r")
        str_1 = str(file.read())  # пишем шифрованное значение счёта
        file.close()
        if str(cryptocode.decrypt(str_1, ScoreBoard.key)) == "False":  # если не расшифровывается
            file = open("score.txt", "w")
            file.write(cryptocode.encrypt("0", ScoreBoard.key))  # пишем шифрованный ноль
            file.close()
            str_1 = 0  # и в переменную ноль
        else:  # если расшифровалось
            str_1 = cryptocode.decrypt(str_1, ScoreBoard.key)  # расшифровываем в переменную счёт
        self.best_score = str_1  # и в переменную лучшего счёта

    def print_score(self, divider=1):  # печать счёта
        self.score += 1  # изменение
        text = "HI " + (5 - len(str(self.best_score))) * "0" + str(self.best_score) + " " + \
               (5 - len(str(self.score // divider))) * "0" + str(self.score // divider)  # формируем строку
        font = pygame.font.Font(ScoreBoard.font_name, 20)  # генерируем шрифт
        text_surface = font.render(text, True, (120, 120, 120))  # рендерим текст
        text_rect = text_surface.get_rect()  # получаем размеры теста
        text_rect.midtop = (1150, 30)  # размещаем
        screen.blit(text_surface, text_rect)  # рисуем

    def save_score(self, divider=1, save_another=-1):  # сохранение
        if self.score // divider > int(self.best_score):  # если набрали больше лучшего
            file = open("score.txt", "w")
            if save_another == -1:  # если не надо сохранить другое
                file.write(cryptocode.encrypt(str(self.score // divider), ScoreBoard.key))  # шифруем и пишем лучшее
            else:  # если надо
                file.write(cryptocode.encrypt(str(save_another), ScoreBoard.key))  # пишем другое
            file.close()  # закрываем

    def get_score(self):
        return self.score
