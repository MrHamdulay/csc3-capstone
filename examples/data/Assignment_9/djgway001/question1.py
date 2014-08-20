#interpreting data from a list and giving the appropriate command
#wayne de jager
#14 may 2014

import math

filename=input("Enter the marks filename:\n")

file=open(filename,"r")
rawlist=file.readlines()
file.close()

modlist=[]
for i in range(0,len(rawlist)-1):
    modlist.append(rawlist[i][0:-1])
modlist.append(rawlist[len(rawlist)-1]) #removes "\n" from each item in the list

modlist2=[]
for i in range(0,len(modlist)):
    divterm=modlist[i].split(",")
    modlist2.append(divterm) #splits names and marks, list alternates name and marks

numlist=[]
for i in range(0,len(modlist2)):
    numlist.append(eval(modlist2[i][1])) #generates a list of intergers in original order
wordlist=[]
for i in range(0,len(modlist2)):
    wordlist.append(modlist2[i][0]) #generates a list of names in original order


def meanval(x):
    mean=round((sum(x)/len(x)),2)
    return mean #returns the mean of list_x

def standardev(x):
    N=len(x)
    M=meanval(x)
    total=0
    for i in range(N):
        total=total+(x[i]-M)**2
    standev=round(math.sqrt(total/N),2)
    return standev #returns the standard deviation of list_x


def advisor(x):
    average=meanval(x)
    stddev=standardev(x)
    studentlist=[]
    checklist=[]
    print("The average is:","%2.2f"%average)
    print("The std deviation is:","%2.2f"%stddev)
    for i in range(0,len(x)):
        if numlist[i]<(average-stddev):
            studentlist.append(wordlist[i])
    if studentlist!=checklist:
        print("List of students who need to see an advisor:")
        for i in range(0,len(studentlist)):
            print(studentlist[i]) #if mark is lower then 1 standev, print corresponding name

advisor(numlist)