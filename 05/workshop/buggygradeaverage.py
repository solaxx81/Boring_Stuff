def calculate_grade_average(grade_sum, number_of_grades):
    """Calcule de la moyenne"""
    grade_average = int(grade_sum / number_of_grades)
    return grade_average


counter = 0
total = 0
while True:
    print('Enter a grade, or "done" if done entering grades:')
    grade = input()
    if grade == "done":
        counter=1
        break
    counter = counter + 1
    total = total + int(grade)

avg = calculate_grade_average(total, counter)
print("The grade average is:", avg)
