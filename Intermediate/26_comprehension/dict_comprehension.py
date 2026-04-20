names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]

# create a dict using a random score of a list
import random
student_scores = {student:random.randint(1, 100) for student in names}
print(student_scores)

# create a dict using dict comprehension
passed_students = {student:score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

# Count words including punctuation
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words_list = sentence.split(' ')
print(words_list)
result = {word:len(word) for word in words_list}
print(result)


# Do the weather
weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(degrees_c*9/5)+32 for (day, degrees_c) in weather_c.items()}

print(weather_f)