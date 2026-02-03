# importing the modules that I will need
import pandas

# creating the student data frame and saving the csv file to it
student_data_frame = pandas.read_csv("student.csv")

# filtering the student data frame based on the questions requirements
filtered_students_data_frame = student_data_frame[(student_data_frame['studytime'] >= 3) & (student_data_frame['absences'] <= 5) & (student_data_frame['internet'] == 1)]

# saving the data frame to a csv file named high engagement
filtered_students_data_frame.to_csv("high_engagement.csv", index=False)

# calculating the number of students in the high engagement
num_of_students = len(filtered_students_data_frame)

# calculating the average grade of the high engagement students
total_grade = 0
for grade in filtered_students_data_frame['grade']:
    total_grade += grade

average_grade = total_grade/num_of_students

# printing the number of students and the average grade in the high engagement
print(f"The number of students saved: {num_of_students}")
print(f"The average grade was: {average_grade:.2f}")
