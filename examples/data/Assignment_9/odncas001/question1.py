"""program to determine necessity of student-student advisor consultations
casey o'donnell
12 may 2014"""

import math

filename=input("Enter the marks filename:\n")

f=open(filename,"r")
linelist=f.readlines()
f.close()

def file_array(l):
    #convert the info from readlines function into a useable array
    array=[]
    for line in l:
        array.append(line.split(","))
    return array

def mean(l):
    n=len(l)
    #calculate the mean score (mu)
    total=0
    for line in range(n):
        total+=eval(l[line][1])
    mu=total/n
    return mu

def stand_dev(l,mu):
    """determine the standard deviation from marks in file"""
    n=len(l)
    #calculate numerator of stddev
    numerator=0
    for line in range(n):
        numerator+=(eval(l[line][1])-mu)**2
    #calculate the stddev (theta)
    theta=numerator/n
    return math.sqrt(theta)

def advise_check(l,mu,theta):
    student_list=[]
    for line in range(len(l)):
        if eval(l[line][1])<mu-theta:
            student_list.append(l[line][0])
    return student_list
                
l=file_array(linelist)
mu=mean(l)
theta=stand_dev(l,mu)
final_list=advise_check(l,mu,theta)
print("The average is: {0:.2f}".format(mu))
print("The std deviation is: {0:.2f}".format(theta))
if final_list!=[]:
    print("List of students who need to see an advisor:")
for i in final_list:
    print (i)

        
    