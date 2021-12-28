from question_model import Question
from quiz_brain import QuizBrain
from data import question_data


question_database = []
for question in question_data:
    question_database.append(Question(question))

quizzes = QuizBrain(question_database)

while quizzes.has_more_question():
    quizzes.display_question()

print("You've completed the quiz")
print(f"You final score was: {quizzes.score}/{quizzes.question_num}")