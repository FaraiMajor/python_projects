from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

question_bank = []

# when we loop each index return a dictionary and from the dictionary we calls values by keys
for question in question_data:
    q_text = question['text']
    q_ans = question['answer']
    new_question = Question(q_text, q_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
print(logo)
while quiz.has_questions():
    quiz.next_question()
