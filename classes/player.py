from classes.riddle import Riddle


class Player:
    def __init__(self):
        self.score = 0
        self.riddles = Riddle()
        self.current_riddle = None

    def reset_game(self):
        self.score = 0
        self.riddles = Riddle()
        self.current_riddle = None

    def get_next_riddle(self):
        self.current_riddle = self.riddles.get_riddle()
        return self.current_riddle

    def get_score(self):
        return {'value': self.score}

    def check_answer(self, answer):
        if not self.current_riddle:
            return {'is_correct': False}

        correct = answer.strip().lower() == self.current_riddle.get('answer').strip().lower()
        if correct:
            self.score += 1

        return {
            'riddle': self.current_riddle['text'],
            'is_correct': correct,
            'answer': self.current_riddle['answer']
        }
