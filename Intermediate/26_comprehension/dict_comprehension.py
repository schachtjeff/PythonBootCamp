names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# create a dict using a random score of a list
import random
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# create a dict using dict comprehension
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)