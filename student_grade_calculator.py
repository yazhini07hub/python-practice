name = input("Enter student name: ")

marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n----- Student Result -----")
print("Name:", name)
print("Total:", total)
print("Percentage:", percentage)
print("Grade:", grade)