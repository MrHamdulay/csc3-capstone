"""Program to read marks from text file
Paul Truter
12 May 2014"""

import math
#get input from user
file=input("Enter the marks filename:\n")

#open file and read lines in file
f=open(file,"r")
lines=f.readlines()
f.close()

#get mark values
marklist=[]    
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    position=lines[i].index(",")
    marklist.append(lines[i][position+1:])

#get average
sum_marks=0
for i in marklist:
    sum_marks+=int(i)
    average=sum_marks/(len(marklist))

#get standard deviation
sum_marks2=0
for i in marklist:
    sum_marks2+=(int(i)-average)**2
    std_deviation=round(math.sqrt(sum_marks2/len(marklist)),2)
    
#get list of names
names=[]    
for i in range(len(lines)):
    lines[i] = lines[i][:-1]
    position=lines[i].index(",")
    names.append(lines[i][:position])

#students that needs to see advisor
advisor_list=[]
for i in range(len(marklist)):
    if int(marklist[i])<(average-std_deviation):
        advisor_list.append(names[i])
        
print("The average is:",'{0:0.2f}'.format(average))
print("The std deviation is:",'{0:0.2f}'.format(std_deviation))
if len(advisor_list) >= 1:
    print("List of students who need to see an advisor:")
    for i in advisor_list:
        print(i)
else:
    print("")



