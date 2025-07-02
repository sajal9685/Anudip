marks = []
for i in range(5):
    marks.append(float(input(f"Enter marks for subject {i+1}: ")))
total = sum(marks)
percentage = total / 5
if percentage >= 60:
    print("First division")
elif percentage >= 50:
    print("Second division")
elif percentage >= 40:
    print("Third division")
else:
    print("Fail")
