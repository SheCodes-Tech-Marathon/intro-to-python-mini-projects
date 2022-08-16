from random import randint


class Engine:
    def __init__(self):
        self.guessing_number = randint(1, 100)

    def is_right(self, number):
        if number == self.guessing_number:
            return True
        else:
            return False
        