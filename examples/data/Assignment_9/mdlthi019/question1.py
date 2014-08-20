"""Program to analyse student marks read in from a file and determine which students need to see a student advisor 
Thiloshni Moodley
17 May 2014"""

import math

file=input("Enter the marks filename:\n") 
f = open(file,"r") # open file
lines=f.readlines()
f.close() # close file

marks=[] # create empty list for marks
names=[] #create empty list for names

#works out average
average=0 #initialise the average to 0
for x in range(len(lines)):
    marks.append(lines[x].split(',')[1].split("\n")[0]) #removes new line character
    names.append(lines[x].split(',')[0]) #adds to list
    marks[x]=int(marks[x]) #converts marks to integers
    average+=marks[x]
average=average/len(marks) #formula for average, float division

#works out standard deviation
standard_deviation=0
for x in range(len(marks)):
    standard_deviation+=(marks[x]-average)**2 
standard_deviation=math.sqrt(standard_deviation/len(marks)) #formula for standard deviation

#output statements with formatting
print("The average is:","{:.2f}".format(average)) 
print("The std deviation is:","{:.2f}".format(standard_deviation))
case=False

for x in range(len(marks)):
    if(marks[x]<(average-standard_deviation)):
        case=True
        
#students that need to see advisor
if(case): #if the case is true execute below
    print("List of students who need to see an advisor:")
    for x in range(len(marks)):
        if(marks[x]<(average-standard_deviation)):
            print(names[x])
