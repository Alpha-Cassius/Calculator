# Stage 3: Student Grade and Percentage Calculator
name = input("Enter Student Name: ")
m1 = float(input("Subject 1 Marks (0-100): "))
m2 = float(input("Subject 2 Marks (0-100): "))
m3 = float(input("Subject 3 Marks (0-100): "))

total = m1 + m2 + m3
percentage = (total / 300) * 100

if percentage >= 75:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print(f"\n{name}")
print(f"Total: {total}/300")
print(f"Percentage: {percentage:.1f}%")
print(f"Grade: {grade}")
