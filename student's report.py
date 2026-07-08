print("======================================")
print("     STUDENT RESULT MANAGEMENT SYSTEM")
print("======================================")
name = input("Enter Student Name: ")
age = int(input("Enter Student Age: "))
department = input("Enter Department: ")
subjects = ["Science", "Social", "Maths", "Hindi", "English"]
marks = []
for subject in subjects:
    mark = int(input("Enter " + subject + " mark: "))
    marks.append(mark)
total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)
highest = marks[0]
for mark in marks:
    if mark > highest:
        highest = mark
lowest = marks[0]

for mark in marks:
    if mark < lowest:
        lowest = mark
passed_count = 0
failed_count = 0
for mark in marks:
    if mark >= 35:
        passed_count = passed_count + 1
    else:
        failed_count = failed_count + 1
if failed_count == 0:
    result = "PASS"
else:
    result = "FAIL"
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "E"
for i in range(len(subjects)):
    if marks[i] >= 35:
        print(subjects[i], ":", marks[i], "- Pass")
    else:
        print(subjects[i], ":", marks[i], "- Fail")
print("\n======================================")
print("        STUDENT REPORT")
print("======================================")
print("Name          :", name)
print("Age           :", age)
print("Department    :", department)
print("--------------------------------------")
print("Total Marks   :", total)
print("Average Marks :", average)
print("Highest Mark  :", highest)
print("Lowest Mark   :", lowest)
print("Subjects Passed :", passed_count)
print("Subjects Failed :", failed_count)
print("Grade         :", grade)
print("Result        :", result)
print("======================================")
