name = input("Enter student name")
num_subjects = int (input (f"enter the number of subjects :"))
total_grade_points = 0
for i in range(num_subjects):
    grade_point = float(input(f"enter grade point for subjects {1+i}:v"))
    total_grade_points += grade_point
cgpa = total_grade_points/num_subjects

print("\n----Student Result----")
print("Student Name:", name)
print("CGPA :", round(cgpa,2))