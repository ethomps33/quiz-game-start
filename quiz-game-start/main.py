from question_base import Question
from data import question_data
from quiz_brain import QuizBrain

ques_bank = []
for ques in question_data:
    new_ques = Question(ques['text'], ques['answer'])
    ques_bank.append(new_ques)

quiz = QuizBrain(ques_bank)
quiz.next_question()

cont_quiz = quiz.still_has_ques()

while cont_quiz:
    quiz.next_question()
    cont_quiz = quiz.still_has_ques()

# turns = 0
# random.shuffle(question_data)


# def playgame():
#
#     for ques in question_data:
#         question = question_base.Question(ques['text'])
#         answer = ques['answer']
#         print(question)
#         #
#         score = Checker(answer, turns)
#         print(score)
#
#
#
#
