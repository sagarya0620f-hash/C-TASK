marks = []

for i in range(1, 6):
    mark = float(input(f"Enter Marks for Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("\nTotal Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)