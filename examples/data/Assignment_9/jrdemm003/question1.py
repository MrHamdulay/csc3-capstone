"""Write a Python program to analyse student marks read in from a file and determine which students need to see a student advisor. The students who (hypothetically!) need to see a student advisor are those with marks less than one standard deviation below the mean.

The marks file is composed of lines of text, where each line contains a student number and mark separated by a comma.

Remember that the formula for standard deviation is:

σ = sqrt (((x 0 -µ)2+(x 1 -µ)2 +(x 2 -µ)2 +…+(x N -1 -µ)2) / N)

where µ is the mean or average and each x i is a mark.

Before the list of student names, print out the average and standard deviation with 2 decimal points of precision.

Sample File (test1.txt)

Alan,35
Siobhan,23
Mmberengeni,38

Sample I/O

Enter the marks filename:
test1.txt
The average is: 32.00
The std deviation is: 6.48
List of students who need to see an advisor:
Siobhan"""

"""ASSIGNMENT 9, QUESTION 1- COMPUTING STANDARD DEVIATIONS AND MARKS
EMMA JORDI
10 MAY 2014"""

import math
numbers = []
names = []
file = input("Enter the marks filename:\n")
f=open(file,"r")
#file= open(textfile, "r")

lines=[]
for line in open(file, "r"):
    lines.append(line)
f.close()

for line in lines:
    for ch in line:
        position=line.find(",")
    names.append(line[:position]) #creates a list of the names
    numbers.append(line[position+1:position+3]) #cuts off newline and creates a list of the marks


def mean(numbers):
    f="{0:0.2f}"
    summ=0
    for i in numbers:
        summ = summ + eval(i)
        m = summ/int(len(numbers))  
    return m
   
def stddev(numbers):
    
    length=len(numbers)
    total= 0
    m = mean(numbers)
    
    for i in range(length):
        total+= (eval(numbers[i])- m)**2
    under_root= total *1.0/length
    stddeviation = math.sqrt(under_root)
    return stddeviation

failed_students = {}
cutoff= mean(numbers) - stddev(numbers)
for n in range(len(numbers)):
    mark= numbers[n-1]
    if  eval(mark) < cutoff:#check <=
        failed_students [numbers[n-1]] =names[n-1]
        
    #FORMAT TO 2.00
f="{0:0.2f}"      
        
print("The average is:",f.format(round(mean(numbers),2))) 
print("The std deviation is:",f.format(round(stddev(numbers),2)))
if failed_students =={}:
    print()
else:
    print("List of students who need to see an advisor:")
#failed_students= failed_students.values()
for student in failed_students:
    print(failed_students[student]) #needs to print out only the name

