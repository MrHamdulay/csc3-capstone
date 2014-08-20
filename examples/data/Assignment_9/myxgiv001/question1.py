"""Python program that reads files
Given Moyo
19 May 2014"""



 # to Create a new file
filename = input("Enter the marks filename:\n") 
  # opening file
file = open(filename,"r")
# to read everything into a list of strings
students = file.readlines()
 # closing the file
file.close()                                    

                                 
totalMarks = 0
# to iterate over the list to split the student number and mark 
for student in students:
    items = student.split(",")                 
    totalMarks += eval(items[1])
    
       # calculating the mean
mean = round(totalMarks/len(students),2)

squaredSDV = 0
for student in students:
    items = student.split(",")
    squaredSDV += (eval(items[1])-mean)**2
    
# to calculate the standard deviation
SDV = round((squaredSDV/len(students))**0.5 ,2) 

print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(SDV))

  # to analyse and see students with marks less than one standard deviation below the mean
for student in students:                      
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):
        print("List of students who need to see an advisor:")
        break
        
        
        
for student in students:                        
    items = student.split(",")
    if eval(items[1]) < (mean - SDV):        
        print(items[0])