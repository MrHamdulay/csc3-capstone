# Najeeb Sirkhoth
# SRKMOH002
# question1.py
# Assignment 9 


import math 
filename = input("Enter the marks filename:\n") 
 


# Calculate mean mark
infile = open(filename, "r")
total = 0
count = 0
for i in infile:    
    name, mark = i.split(",")                  # Extract marks from string
    mark1 = eval(mark)
    total += mark1                             # Accumulate marks to total
    count += 1                                 # Keep track of n

mean = total/count   
infile.close()


# Calculate value of 1 standard devaition
infile = open(filename, "r")
sumofsquares = 0
for i in infile: 
    name, mark = i.split(",")       
    mark1 = eval(mark)
    square = (mark1-mean)**2                   # Calculate deviation squares     
    sumofsquares += square                     # Accumulate to sum of squares
  
meansquare = sumofsquares/count                # Calculate average square
stddev = math.sqrt(meansquare)                 # Sqrt average square
infile.close() 
 

# Students who need to see student Advisor
infile = open(filename, "r")
students = []
for i in infile: 
    name, mark = i.split(",")
    mark1 = eval(mark)
    if mark1 < (mean-stddev):                 # Only students below 1 std.dev
        students.append(name)                 # Accumulate names of students



print("The average is: {0:0.2f}".format(mean))
print("The std deviation is: {0:0.2f}".format(stddev))
if stddev > 0:
    print("List of students who need to see an advisor:")
    for i in students:
        print (i) 
    
                        

    

    


