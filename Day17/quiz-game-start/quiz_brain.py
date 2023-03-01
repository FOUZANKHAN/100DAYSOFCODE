class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def nextquestion(self):
        currentquestion = self.question_list[self.question_number] #question object
        self.question_number += 1
        userans = input(f"Q.{self.question_number}: {currentquestion.text} (True/False)?: ")
        self.check_answer(userans, currentquestion.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, u_input,cor):
        if u_input.lower() == cor.lower():
            self.score += 1
            print(f"That is the correct answer")
        else:
            print("Wrong")
        print(f"The correct answer is  {cor}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

