from question_base import Question
from data import question_data


ques_bank = []

for ques in question_data:
    new_ques = Question(ques['text'], ques['answer'])
    ques_bank.append(new_ques)
print(ques_bank[0].text)

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
