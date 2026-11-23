
print("===== STUDENT INFORMATION =====")

student_name = input("Enter the Student Name: ")

marks_scored = [
    int(input("Enter English Marks: ")),
    int(input("Enter Maths Marks: ")),
    int(input("Enter Science Marks: ")),
    int(input("Enter Biology Marks: ")),
    int(input("Enter Social Marks: "))
]

college_name = input("Enter Your College Name: ")
department = input("Enter Your Respective Department: ")

total_marks = sum(marks_scored)
average_marks = total_marks / len(marks_scored)
highest_marks = max(marks_scored)
lowest_marks = min(marks_scored)

print("\n===== STUDENT DETAILS =====")

print("Student Name:", student_name)
print("College Name:", college_name)
print("Department:", department)
print("Marks Scored:", marks_scored)

print("\n===== ACADEMIC PERFORMANCE =====")

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Highest Marks:", highest_marks)
print("Lowest Marks:", lowest_marks)
