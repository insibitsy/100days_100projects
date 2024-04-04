grades = []

grade = float(input("Input a grade:"))
grades.append(grade)

grade = float(input("Input a grade:"))
grades.append(grade)

grade = float(input("Input a grade:"))
grades.append(grade)

grade = float(input("Input a grade:"))
grades.append(grade)



avg = sum(grades)/len(grades)
print(grades)
print(f'{avg:.2f}')
name = input("Enter your name:")

students = {name: grades}
print(students)