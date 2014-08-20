#GNPBHO001





filename = input("Enter the marks filename:\n")  # Creating a new file
file = open(filename,"r")                        
students = file.readlines()                       
file.close()                                     

                                 
totalMarks = 0

for student in students:
    items = student.split(",")                 
    totalMarks += eval(items[1])

mean = round(totalMarks/len(students),2)       #mean value

squaredSDV = 0
for student in students:
    items = student.split(",")
    squaredSDV += (eval(items[1])-mean)**2

SDV = round((squaredSDV/len(students))**0.5 ,2) # find SD

print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(SDV))

for student in students:                        
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):
        print("List of students who need to see an advisor:")
        break
        
        
        
for student in students:                        
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):        
        print(items[0])