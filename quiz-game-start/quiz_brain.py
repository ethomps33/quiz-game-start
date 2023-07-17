class QuizBrain:

    def __init__(self, list):
        self.ques_number = 0
        self.ques_list = list
        self.score = 0
        self. current_ques = self.ques_list[self.ques_number]

    def check_answer(self, answer, correct_answer):
        if correct_answer == answer:
            self.score += 1
            print("That is the correct answer!\n"
                  f"Your score is {self.score}/{self.ques_number}")
        else:
            print("That is not the correct answer\n"
                  f"The correct answer was {correct_answer}\n"
                  f"Your score is {self.score}/{self.ques_number}")

    def still_has_ques(self):
        return self.ques_number < len(self.ques_list)

    def next_question(self):
        self.ques_number += 1
        answer = input(f"Q.{self.ques_number} {self.current_ques.text} (True/False): ").title()
        correct_answer = self.current_ques.answer
        QuizBrain.check_answer(self,answer,correct_answer)
