# Khyati Jinerdeb
# Asssignment 9
# Date: 17.05.2014
# To analyse student marks read from a file


filename = input("Enter the marks filename:\n")  # To create a new file
file = open(filename,"r")                        # To open the file
students = file.readlines()                      # To read everything into a list of strings
file.close()                                     # To close file

                                 
totalMarks = 0
# iterating over the list to split the student number and mark 
for student in students:
    items = student.split(",")                 
    totalMarks += eval(items[1])
    
#To calculate the mean
mean = round(totalMarks/len(students),2)      

squaredSDV = 0
for student in students:
    items = student.split(",")
    squaredSDV += (eval(items[1])-mean)**2

#To calculate standard deviation
SDV = round((squaredSDV/len(students))**0.5 ,2) 

print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(SDV))

for student in students:                        
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):
        print("List of students who need to see an advisor:")
        break
        
        
#To print output        
for student in students:                        
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):        
        print(items[0])