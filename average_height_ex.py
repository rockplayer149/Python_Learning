# Dont change the code below
student_heights = input("Input a list of student heights").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
# Dont change the code below
# Write down your code below this row

#This below code is written without for loop
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)

#Using for loop
total_height = 0 #calculating height using for loop
for height in student_heights:
    total_height += height
print(total_height)  

number_of_students = 0
for students in student_heights: 
    number_of_students += 1
print(number_of_students)   