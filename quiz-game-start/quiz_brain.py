from data import question_data
import main



class Checker:

    def __init__(self, answer):
        self.answer = answer
        self.score = main.score
        self.turns = main.turns
    def brain(self):
        self.answer = question_data[0]['answer']
        if self.answer == main.answer:
            self.score +=1
            print("You got it right!\n"
                  f"The answer was: {self.answer}\n"
                  f"Your score is now: {self.score}/{self.turns}")
        else:
            print("That's Wrong.\n"
                  f"The correct answer was: {self.answer}\n"
                  f"Your score is now: {self.score}/{self.turns}")
