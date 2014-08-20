"""Assignment 9 Question 1
Miengha Behardien: BHRMIE001
12 May 2014"""

import math

def average(file):
    """calculates the average of the retrieved
    numbers in a file"""
    f=open(file, "r")
    lines=f.readlines()
    f.close()
    count=0
    mean=0
    for i in lines:
        count+=1
    for line in lines:
        if line[-1]=="\n":
            line=line[:-1]
        line=line.split(",")
        mean+=eval(line[1])
    return str(round(mean/count,2))

def deviation(file):
    """calculates the standard deviation of 
    numbers retrieved from a file"""
    f=open(file, "r")
    lines=f.readlines()
    f.close()
    count=0
    for i in lines:
        count+=1
    mean=eval(average(file))
    standard=0
    for line in lines:
        if line[-1]=="\n":
            line=line[:-1]
        line=line.split(",")
        standard+=(eval(line[1])-mean)**2
    dev=str(round(math.sqrt(standard/count),2))
    return dev

def marks(file):
    """determines which of the students require
    to see the student advisor"""
    f=open(file, "r")
    lines=f.readlines()
    f.close()
    mean=eval(average(file))
    dev=eval(deviation(file))
    names=[]
    for word in lines:
        if word[-1]=="\n":
            word=word[:-1]
        new_word=word.split(",")
        mark=eval(new_word[1])
        if mark < mean-dev:
            names.append(new_word[0])
    return names

def main():
    file=input("Enter the marks filename:\n")
    print("The average is:", "{0:0<5}".format(average(file)))
    print("The std deviation is:", "{0:0<4}".format(deviation(file)))
    x=marks(file)
    if x:
        print("List of students who need to see an advisor:")
        for i in x:
            print(i)
    
main()    