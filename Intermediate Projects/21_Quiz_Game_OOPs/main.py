from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import pyfiglet
logo = pyfiglet.figlet_format("Test your Brain")
print(logo, end="-" * 80 + "\n" + "-" * 80 + "\n")

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"your final score was {quiz.score}/{quiz.question_number}")

