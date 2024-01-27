class Speed:
    def __init__(self):
        super().__init__()
        self.speed_cof = 0

    def add_speed(self, add=0.1):
        self.speed_cof += add

    def get_speed(self):
        return self.speed_cof
