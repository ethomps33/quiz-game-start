from data import question_data
import random


class Question:

    def __init__(self, text):
        self.text = text

    def quiz(self):
        random.shuffle(question_data)
        self.text = question_data[0]['text']
        print(self.text)
