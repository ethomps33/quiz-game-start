class QuizBrain:

    def __init__(self, list):
        self.ques_number = 0
        self.ques_list = list

    def still_has_ques(self):
        return self.ques_number < len(self.ques_list)

    def next_question(self):
        current_ques = self.ques_list[self.ques_number]
        self.ques_number += 1
        answer = input(f"Q.{self.ques_number} {current_ques.text} (True/False): ").lower()

