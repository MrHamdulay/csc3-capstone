"""Name: Sibulele Hlongwane 
Date: 13 May 2014
Assignment: Determine student who needs to see a student advisor: files"""
import math
"""prompt user to enter filename, therefore open and read lines into a list"""
filename= input("Enter the marks filename:\n")
f=open(filename,"r")
lines=f.readlines()

"""initialising of values to be used"""
average=0

Sum=0
marks=[]
deviationcalc=0
standarddeviation=0
positions=[]
lowestacceptablemark=0
names=[]
#students needing to see student advisors list
salist=[]
for j in range(len(lines)-1):
    lines[j]= lines[j][:-1]

#print(lines[0])

"""Finds the position of the comma"""
for j in range(len(lines)):
    position= lines[j].index(",")
    marks.append(lines[j][position+1:])
    names.append(lines[j][:position])

"""Determines the mark average of students"""
for j in range(len(marks)):
    Sum=Sum+ int(marks[j])
average=Sum/len(marks)
 

"""Determine standard deviation"""
for j in range(len(marks)):
    deviationcalc= deviationcalc+ (((int(marks[j]))-average)**2)
standarddeviation=((deviationcalc)/len(marks))**(1/2)


"""Determine students needing to see student advisor"""
lowestacceptablemark=average-standarddeviation

for j in range(len(marks)):
    if int(marks[j])<(average-standarddeviation):
        salist.append(names[j])
        
        
"""Displays output"""
print("The average is:", "{0:.2f}".format(average))
print("The std deviation is:", "{0:.2f}".format(standarddeviation))
if len(salist)!=0:
    print("List of students who need to see an advisor:")
for j in salist:
    print(j)


f.close()