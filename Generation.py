import random


class Generation:
    """ Return values:
        -1
        0 - Cactus
        1 - Bird
        2 - Tumbleweed
        3 - Tree """
    def __init__(self):
        super().__init__()
        self.last_distance_jump = 0
        self.double_cactus = 0
        self.double_bird = 0

    def generate(self, one_jump, speed, speed_coef=25 / 15, frequency=0.085, random_tree=0.0025):
        self.last_distance_jump -= 15
        self.double_cactus -= 1
        self.double_bird -= 1
        if random.random() < frequency:
            if random.random() < 0.7:
                if self.last_distance_jump + 0.2 * speed + one_jump < speed or self.last_distance_jump <= 1300:
                    self.last_distance_jump = speed + one_jump * 2
                    if random.random() < 0.2:
                        self.double_cactus = 10
                    if random.random() < 0.8:
                        return [0]
                    else:
                        return [2, 1920 + 1920 * speed_coef * 1.5]
            else:
                if self.last_distance_jump + 0.2 * speed + one_jump < speed or self.last_distance_jump <= 1300:
                    self.last_distance_jump = speed + one_jump * 2
                    if random.random() < 0.2:
                        self.double_bird = 15
                    return [1, 1920 + 1920 * speed_coef * 1.5]
        elif self.double_cactus == 0 or self.double_bird == 0:
            if self.double_cactus == 0:
                if self.last_distance_jump + 0.2 * speed + one_jump < speed:
                    self.last_distance_jump = speed + one_jump * 2
                    if random.random() < 0.2:
                        self.double_cactus = 10
                    if random.random() < 0.8:
                        return [0]
                    else:
                        return [2, 1920 + 1920 * speed_coef * 1.5]
            else:
                if self.last_distance_jump + 0.2 * speed + one_jump < speed:
                    self.last_distance_jump = speed + one_jump * 2
                    if random.random() < 0.2:
                        self.double_bird = 15
                    return [1, 1920 + 1920 * speed_coef * 1.5]
        if random.random() < random_tree:
            return [3]
        return [-1]
