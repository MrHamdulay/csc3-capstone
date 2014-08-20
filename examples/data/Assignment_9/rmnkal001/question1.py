#Kalind Ramnarayan
#Reading student marks from a file
#11 May 2014

import math

filename=input("Enter the marks filename:\n")          #Open the file
f = open(filename,"r")
lines=f.readlines()
marks=[]                                               #Create 2 empty lists
names=[]
mean=0
for i in range(len(lines)):
    marks.append(lines[i].split(',')[1].split("\n")[0])  # take info from file put it in list
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    mean+=marks[i]
    
mean=mean/len(marks)                               #find mean             
sd=0

for i in range(len(marks)):                         #find stanard deviation
    sd+=(marks[i]-mean)**2
sd=math.sqrt(sd/len(marks))

print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(sd))
help=False

for i in range(len(marks)):                        #check who needs an advisor
    if(marks[i]<(mean-sd)):
        help=True
        
if(help):
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if(marks[i]<(mean-sd)):
            print(names[i])

