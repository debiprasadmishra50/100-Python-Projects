from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUI

question_bank = []  # Will contain Question Objects, 10 questions
for question in question_data:
    question_text = question['question']
    answer_text = question['correct_answer']
    new_question = Question(q_text=question_text, q_answer=answer_text)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizUI(quiz)
