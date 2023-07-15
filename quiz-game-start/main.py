from data import question_data
from question_model import Question
from quiz_brain import Checker
import random


global score
score = 0
global turns

random.shuffle(question_data)


def playgame():

    for ques in question_data:

        text = ques['text']
        answer = ques['answer']
        turns += 1
        Question(text)
        score = Checker(answer)




