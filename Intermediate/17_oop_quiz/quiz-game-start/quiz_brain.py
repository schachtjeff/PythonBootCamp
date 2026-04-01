# Quiz Brain class takes number of questions and question list


class QuizBrain:
    def __init__(self, q_list, q_number = 0):
        self.question_number = q_number
        self.question_list = q_list

    def next_question(self):
        the_data = self.question_list[self.question_number]
        self.question_number +=1
        user_answer = input(f"Q.{self.question_number}: {the_data.text}. (True/False)?: ")

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)
