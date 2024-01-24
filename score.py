student_scores = {
    "Marion": 92,
    "Shalom": 99,
    "Hope": 67,
    "Lavender": 76,
    "Mirriam": 87,
    "Talash": 60
}
# TODO-1: Create an empty dictionary called student_grades

student_grades = {}

# TODO-2:  Write your code below to add the grade to student_grades
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding "
    elif score > 80:
        student_grades[student] = "Exceeding expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Failure!"

print(student_grades)
