# Weighted Exam Score Average

# Entering how many exams I have done
number_of_exams = int(input('enter number of exams: '))
print(number_of_exams)

# Entering how many credits these exams cover
total_credits = int(input('enter how many credits these exams cover: '))
print(total_credits)

# Being with average of 0 and then add up percentages from each exam
average = 0
for exam in range(number_of_exams):
    score = int(input('enter exam score: '))
    exam_credits = int(input('enter how many credits this exam covered: '))
    average = average + score*exam_credits/total_credits
print('your average is', average)
