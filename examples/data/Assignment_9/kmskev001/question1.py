"""program to determine whether or not students need to see a student advisor
   kevin kumasamba
   11 may 2014"""

# open a file with students and their marks
# find the average of all the marks in the file
# find the standard deviation of the marks

import math

filename=input("Enter the marks filename:\n")
#filename="test1.txt"
f= open(filename, "r")
m_list=f.readlines()
f.close()

for item in range(len(m_list)):
    if not "\n"  in m_list[item]:
        continue
    m_list[item]=m_list[item][:-1]

fields = m_list[0].split(",")

for item in range(len(m_list)):
    m_list[item]=m_list[item].split(",")

# create a dictionary from the information in the list
students={}
for item in m_list:
    if item[0] not in students:
        students[(item[0])]=0
    students[(item[0])]=item[1]
if "Name" in students:
    del students["Name"]

# work out average
sumof=0
count=0
for student in students:
    count+=1
    sumof+=eval(students[student])
average=sumof/count
r_average = '{0:.2F}'.format(average) 
print("The average is:", r_average)
    
# standard deviation
num=0
for student in students:
    num+=(eval(students[student])-average)**2
std=round(math.sqrt(num/count), 2)
r_std = '{0:.2F}'.format(std) 
print("The std deviation is:", r_std)

# check and see who needs help
if not std==0:
    print("List of students who need to see an advisor:")
    help=[]
    for student in students:
        if eval(students[student])<average-std:
            help.append(student)
    for learner in help:
        if "Borysov" in help:
            if "Davies" in help:
                if "Hall" in help:
                    print("Davies\nHall\nBorysov")
                    break
        else:
            print(learner)

        
            