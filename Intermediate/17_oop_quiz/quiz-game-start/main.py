from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

def main() -> None:
    question_bank = []
    # Add question text and answer to object from model.
    for data in question_data:
        question_bank.append(Question(question=data["text"], answer=data["answer"]))

    # print out to validate.
    #for item in question_bank:
    #    print(item.text)
    #    print(item.answer)

    quiz = QuizBrain(question_bank)

    #loop for if there are still questions
    while quiz.still_has_questions():
        quiz.next_question()

    print(f"You've completed the quiz. \n Your final score is {quiz.user_score}/{quiz.question_number}")

main()