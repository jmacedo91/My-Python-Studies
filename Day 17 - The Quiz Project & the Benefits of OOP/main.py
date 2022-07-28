from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_bank = []

for data in question_data:
    question_bank.append(Question(data["question"], data["correct_answer"]))

quiz = QuizBrain(question_bank)

#if quiz still has questions remaining:
while quiz.still_has_questions():
    quiz.next_question()
    quiz.still_has_questions()

print("You've completed the quiz!")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")