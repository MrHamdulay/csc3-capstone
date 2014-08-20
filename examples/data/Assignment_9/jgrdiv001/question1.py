"""program to check marks and analyse marks
Author:Divan Jagers
Date: 12 May 2014"""
from math import *
def check_marks():
    file=input("Enter the marks filename:\n")    #prompts the user for input
    f= open(file, "r")     #opens the file and is in read mode
    data=f.readlines()      #creates a list of each line of the items of names and marks
    f.close()
    marklist=[]         #a marlist without the "\n" character at the end of line
    for i in data:       #an iteration that appens to marklist
        data=i[:-1]
        marklist.append(data)     # appends to the marklist
    slist=[]      #slist is a list of names and marks that are no longer attached to each other but rather become individual names and marks eg([name,mark,name,mark]
    for item in marklist:        #an iteration that appens to the slist and splits each item by a space
        item=item.split(",")
        slist.append(item)
    marks=[]      #the slist is further split up and all the numeric marks are than added to the marks list
    for i in range(len(slist)):
        mark=slist[i][1]
        marks.append(mark)
    students=[]    #the slist is further split up and all the names of students are than added to the students list
    for i in range(len(slist)):
        mark=slist[i][0]
        students.append(mark)     
    total=0     #is used to calculate the mean(each mark is added to the total
    n=0    #number of marks added to total
    for item in marks:   #an iteration that adds the marks to the total counter
        item=eval(item)
        total+=item
        n+=1       #with each mark added the number of item is incremented by 1
    mean=total/n   #mean calculation
    ansM="%.2f" % round(mean,2)   #formats the mean calculation answer
    var=0     #counter for variance
    for i in marks:
        i=eval(i)
        var+=(i-mean)**2   #adds each individual variance to the counter var
    stand_dev=sqrt(var/n)    #calculates the standard deviation
    
    ansS="%.2f" % round(stand_dev,2)   #formats the standard deviation answer
    print("The average is:",ansM)
    print("The std deviation is:",ansS)    #prints mean and standard deviation
    badS=[]    # a list of names of all students who need to see an advisor
    for i in range(len(marks)):
        if eval(marks[i])<(mean-stand_dev):
            badS.append(students[i])   #adds the name indexed by the student list to the badS list
        else:
            continue
    if len(badS)>0:    #prints the list of badS names
        print("List of students who need to see an advisor:")
    for name in badS:
        print(name)
if __name__=="__main__":
    check_marks()