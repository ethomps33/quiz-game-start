# from data import question_data
# import question_base
# question = question_base.Question()
# score = 0
#
#
# class Checker:
#
#     def __init__(self, answer,turns):
#         self.answer = answer
#         self.score = score
#         self.turns = turns
#
#     def brain(self):
#         if self.answer == question.quiz():
#             self.score +=1
#             print("You got it right!\n"
#                   f"The answer was: {self.answer}\n"
#                   f"Your score is now: {self.score}/{self.turns}")
#             return self.score
#         else:
#             print("That's Wrong.\n"
#                   f"The correct answer was: {self.answer}\n"
#                   f"Your score is now: {self.score}/{self.turns}")
#             return self.score
class QuizBrain:

    def __init__(self, list):
        self.ques_number = 0
        self.ques_list = list

    def still_has_ques(self):
        if self.ques_number < len(self.ques_list):
            print(len(self.ques_list))
            return True
        else:
            return False


    def next_question(self):
        current_ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        answer = input(f"Q.{self.ques_number} {current_ques.text} (True/False): ").lower()

