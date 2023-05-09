# students_heights = [180, 124, 165, 173, 189, 169, 146]
#
# number_of_students = len(students_heights)
# print(number_of_students)
#
# sum_of_heights = sum(students_heights)
# print(sum_of_heights)
#
# avg_of_heights = sum(students_heights) / len(students_heights)
# print(avg_of_heights)

students_heights = input("Wpisz wzrost studentów ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

total_height = 0
for height in students_heights:
    total_height += height

number_of_students = 0
for student in students_heights:
    number_of_students += 1

avg_of_heights = round(total_height / number_of_students)
print(avg_of_heights)