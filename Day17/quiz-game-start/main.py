#things that we are supposed to do
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#print(question_data[1]["text"])

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    newq = Question(question_text, question_ans)
    question_bank.append(newq)

new_quiz = QuizBrain(question_bank)
while new_quiz.still_has_question():
    new_quiz.nextquestion()

print("You've completed the quiz omedetto!")
print(f"Your final score is {new_quiz.score} / {len(question_bank)}")


