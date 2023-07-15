from data import question_data
import main
import question_model
given_answer = question_model.Question()


class Checker:

    def __init__(self, answer):
        self.answer = answer
        self.score = main.score
        self.turns = main.turns

    def brain(self):
        self.answer = question_data[0]['answer']
        if self.answer == given_answer.quiz():
            self.score +=1
            print("You got it right!\n"
                  f"The answer was: {self.answer}\n"
                  f"Your score is now: {self.score}/{self.turns}")
            return self.score
        else:
            print("That's Wrong.\n"
                  f"The correct answer was: {self.answer}\n"
                  f"Your score is now: {self.score}/{self.turns}")
            return self.score
