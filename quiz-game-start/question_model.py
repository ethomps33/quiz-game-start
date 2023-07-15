from data import question_data

import main


class Question:

    def __init__(self, text):
        self.text = text

    def quiz(self):
        answer = input(f"Q{main.turns}. {self.text} 'True' or 'False': ")
        return answer
