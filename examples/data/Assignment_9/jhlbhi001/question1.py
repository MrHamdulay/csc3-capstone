# Python program to analyse student marks read in from a file 
# JHLBHI001
# 17 May 2014




filename = input("Enter the marks filename:\n")  # Creating a new file
file = open(filename,"r")                        # opening file
students = file.readlines()                      # reading everything into a list of strings
file.close()                                     # closing the file

                                 
totalMarks = 0
# iterating over the list to split the student number and mark 
for student in students:
    items = student.split(",")                 
    totalMarks += eval(items[1])

mean = round(totalMarks/len(students),2)       # calculating the mean

squaredSDV = 0
for student in students:
    items = student.split(",")
    squaredSDV += (eval(items[1])-mean)**2

SDV = round((squaredSDV/len(students))**0.5 ,2) # calculating the standard deviation

print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(SDV))

for student in students:                        # analysing to see students with marks less than one standard deviation below the mean
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):
        print("List of students who need to see an advisor:")
        break
        
        
        
for student in students:                        
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):        
        print(items[0])