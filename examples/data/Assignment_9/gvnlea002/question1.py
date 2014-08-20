"""leandra govender
16 may 2014
program to analyse students mark from a read in file and calculate standard deviation"""


import math

filename=input("Enter the marks filename:\n")            #ask user for input filename
f = open(filename,"r")                 #open file to read only
lines=f.readlines()
marks=[]                        #create an empty list for marks and an empty list for names
names=[]
mean=0
for i in range(len(lines)):        #use a for loop split the list into names and marks add marks to marks list and names to name list
    marks.append(lines[i].split(',')[1].split("\n")[0])
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    mean+=marks[i]
mean=mean/len(marks)                  #calculate mean
sd=0
for i in range(len(marks)):
    sd+=(marks[i]-mean)**2
sd=math.sqrt(sd/len(marks))                  #calculate standard deviation
print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(sd))
flag=False

for i in range(len(marks)):
    if(marks[i]<(mean-sd)):
        flag=True
if(flag):
    print("List of students who need to see an advisor:")            #print statement
    for i in range(len(marks)):
        if(marks[i]<(mean-sd)):
            print(names[i])
