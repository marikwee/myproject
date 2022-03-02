print()

count = input("Enter number of assignments that contribute to overall grade: ")
print()

count = int(count)

assign = []
weightGrade = []
grades = []
total = 0
finalGrade = 0

for x in range(count):
    assignment = input("Enter name of assignments: ")
    assign.append(assignment)

print()

for i in range(count):
    weight = input("Enter grading weight for " + assign[i] + " (%): ")
    weight = float(weight)
    weight = weight * 0.01
    weightGrade.append(weight)

print()

print("For the following, enter grades for given assignment.")
print("If grade unavailable, enter 'N/A' ")

print()

for j in range (count):
    grade = input("Enter grade for " + assign[j] + " (%): ")
    if (grade != 'N/A'):
        grade = float(grade)
        grade = grade * weightGrade[j]
    grades.append(grade)

for k in range (count):
    if (type(grades[k]) == float):
        total = float(total)
        total = total + weightGrade[k]
        finalGrade = float(finalGrade)
        finalGrade = finalGrade + grades[k]

print()

finalGrade = finalGrade / total
finalGrade = round(finalGrade, 2)

finalGrade = str(finalGrade)

print("Final Grade: " + finalGrade)
print()

if (total < 1):
    for m in range (count):
        testGrade = float(finalGrade)
        if (grades[m] == 'N/A'):
            passingGrade = input("Enter the passing grade for this class: ")
            passingGrade = float(passingGrade)
            temp = float(1 - weightGrade[m])
            testGrade = testGrade * temp
            temp = passingGrade - testGrade
            testGrade = temp / weightGrade[m]
            testGrade = round(testGrade, 2)
            testGrade = str(testGrade)
            print("Lowest grade you can get on " + assign[m] + " is: " + testGrade)
            print()






    
    


