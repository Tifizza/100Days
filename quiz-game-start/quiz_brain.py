class QuizBrain:
    def __init__(self,q_list):

        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def next_question(self):
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {self.question_list[self.question_number - 1].text}(True/False)?:")
        if answer == self.question_list[self.question_number-1].answer:
            self.score += 1
            print("You got it Right !")
            print(f"The correct answer was: {self.question_list[self.question_number - 1].answer}")
            print(f"Your current score is {self.score}/{self.question_number}")
            print("\n")
        else:
            print("That's Wrong.")
            print(f"The correct answer was: {self.question_list[self.question_number-1].answer}")
            print(f"Your current score is {self.score}/{self.question_number}")
            print("\n")
        if self.question_number == len(self.question_list):
            print("You've completed the quizz")
            print(f"Your final score is {self.score}/{self.question_number}")
            return False
        else:
            return True

