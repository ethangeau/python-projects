class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.question_num = 0
        self.score = 0

    def display_question(self):
        question = self.questions[self.question_num]
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {question.text}. (True/False): ").lower()

        if user_answer == question.answer.lower():
            print("You got it right.")
            self.score += 1
        else:
            print("That's wrong.")

        print(f"The correct answer was: {question.answer}.")
        print(f"Your current score is: {self.score}/{self.question_num}")
        print()

    def has_more_question(self):
        return self.question_num < len(self.questions)