"""Program to calculate which students need to see the student advisor
Axel du Plessis
16/05/2014"""

filename = input("Enter the marks filename:\n")
file = open(filename,"r")
students = file.readlines()
file.close()

totalMarks = 0

for student in students:
    items = student.split(",")
    totalMarks += eval(items[1])

mean = round(totalMarks/len(students),2)

squaredSDV = 0

for student in students:
    items = student.split(",")
    squaredSDV += (eval(items[1])-mean)**2

SDV = round((squaredSDV/len(students))**0.5 ,2)
if str(mean)[-2] == ".":
    print("The average is: " + str(mean) + "0")
else:
    print("The average is:", mean)
    
if str(SDV)[-2] == ".":
    print("The std deviation is: "+ str(SDV) + "0")
else:
    print("The std deviation is:", SDV)
    

studentsForAdvisor = False
badStudents = []
for student in students:
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):
        studentsForAdvisor = True
        badStudents.append(items[0])
        
if studentsForAdvisor:
    print("List of students who need to see an advisor:")
    for student in badStudents:
        print(student)