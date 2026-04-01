# Quiz Brain class takes number of questions and question list


class QuizBrain:
    def __init__(self, q_list, q_number = 0):
        self.question_number = q_number
        self.question_list = q_list
        self.user_score = 0

    def next_question(self):
        the_data = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"\n\nQ.{self.question_number}: {the_data.text}. (True/False)?: ")
        self.check_answer(user_answer=user_answer, correct_answer=the_data.answer)


    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer) -> None:
        if user_answer.lower() == correct_answer.lower():
            print("You are correct!")
            self.user_score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is: {self.user_score}/{self.question_number}")
