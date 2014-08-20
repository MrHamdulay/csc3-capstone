"""Assignment 9
Question 1
Micaela Menegaldo
12 May 2014"""

import math

def mean(marks):
    """calculates mean of marks"""
    total=0
    for i in range(len(marks)):
        total+=eval(marks[i][1])
    mean=total/len(marks)
    return mean
    
def standard_deviation(marks,mean):
    """calculates standard deviation of marks"""
    numerator=0
    for i in range(len(marks)):
        numerator+=(eval(marks[i][1])-mean)**2
    standev=math.sqrt((numerator)/(len(marks)))
    return standev

def marks_list(marks,mark):
    """prints out list of students who need to see student advisor"""
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if eval(marks[i][1])>=mark:
            continue
        else:
            print(marks[i][0])
        
    
if __name__=='__main__':
    filename=input("Enter the marks filename:\n")
    names_marks=[]
    marks=[]
    f=open(filename,"r")
    names_marks=f.readlines()
    f.close()
    for item in names_marks:
        marks.append(item.split(","))
    for r in range(len(marks)):
        marks[r][1]=marks[r][1][:len(marks[r][1])-1]

    mean=round(mean(marks),2)
    print("The average is:","{0:0<5}".format(mean))
    stndrddev=round(standard_deviation(marks,mean),2)
    print("The std deviation is:","{0:0<4}".format(stndrddev))
    marktoseeSA=mean-stndrddev
    if marktoseeSA==mean:
        statement = False
    else:
        marks_list(marks,marktoseeSA)
    