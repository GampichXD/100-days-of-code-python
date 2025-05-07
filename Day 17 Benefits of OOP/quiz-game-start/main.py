from question_model import  Question
from data import  question_data
from quiz_brain import QuizBrain

question_bank = []
for i in range(len(question_data["results"])):
    question_bank.append(Question(question_data["results"][i]["question"],question_data["results"][i]["correct_answer"]))


user_1 = QuizBrain(question_bank)
while user_1.still_has_question():
    user_1.next_question()
print("You've completed the quiz")
print(f"Your final score was: {user_1.score}/{user_1.question_number}")




