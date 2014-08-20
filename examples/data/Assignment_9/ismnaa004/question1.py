filename = input("Enter the marks filename:\n")
file = open(filename,"r")
students = file.readlines()
file.close()

form = '{0:0<5}'
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

print("The average is:", form.format(mean))
print("The std deviation is:", SDV)
print("List of students who need to see an advisor:")
for student in students:
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):
        print(items[0])