# Question model class to have 2 attributes of the text and answer.

class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer