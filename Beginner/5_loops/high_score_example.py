student_scores = [180, 124, 165, 173, 189, 169, 146]

#add all the scores
total_exam_scores = sum(student_scores)
print(total_exam_scores)

sum_of_scores = 0
for score in student_scores:
    sum_of_scores += score
# should be the same
print(sum_of_scores)

# Get the largest number
print(max(student_scores))

# Get the largest number using loop
largest_num = 0
for score in student_scores:
    if score > largest_num:
        largest_num = score
        print(largest_num)