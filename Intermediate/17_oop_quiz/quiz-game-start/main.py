from question_model import Question
from data import question_data

def main() -> None:
    question_bank = []
    # Add question text and answer to object from model.
    for data in question_data:
        question_bank.append(Question(question=data["text"], answer=data["answer"]))

    # print out to validate.
    for item in question_bank:
        print(item.text)
        print(item.answer)

main()