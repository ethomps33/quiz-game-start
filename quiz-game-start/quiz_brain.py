class QuizBrain:

    def __init__(self, list):
        self.ques_number = 0
        self.ques_list = list
        self.score = 0

    def check_answer(self, answer, correct_answer):
        if correct_answer == answer:
            self.score += 1
            print("That's right!")
        else:
            print("That is not the correct answer.\n")
        print(f"The correct answer is {correct_answer}\n"
              f"Your score is {self.score}/{self.ques_number}")
        print("\n")

    def still_has_ques(self):
        return self.ques_number < len(self.ques_list)

    def next_question(self):
        current_ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        answer = input(f"Q.{self.ques_number} {current_ques.text} (True/False): ").title()
        correct_answer = current_ques.answer
        QuizBrain.check_answer(self, answer, correct_answer)
