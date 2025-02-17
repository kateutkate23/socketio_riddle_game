from src.all_riddles import riddles
from random import randint


class Riddle:
    def __init__(self):
        self.riddles = riddles[:]

    def get_riddle(self):
        if not self.riddles:
            return None

        index = randint(0, len(self.riddles) - 1)
        return self.riddles.pop(index)
