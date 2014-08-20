"""A program to analyse student marks
Tsanwani Vhonani
12 May 2014"""

import math
def student_marks(filename):
    #Open file and read lines and return the contents as a list with spaces removed
    file = open(filename,'r')
    lines = file.readlines()
    file.close()
    marklist = []
    for line in lines:
        marklist.append(line.replace('\n',''))
    return marklist

def average(marks):
    #Get the average mark rounded off to two decimal places
    count=0
    mean=0 
    for i in marks:
        count=count+1
        if count>0:
            mean=sum(marks)/count
    print("The average is: {:0.2f}".format(mean))
    return mean

def std_dev(mean,marks):
    #Get the std deviation rounded off to two decimal places
    deviation=0
    dif=0
    difference=0    
    for i in marks:
        difference=(i-mean)**2
        dif+=difference
        deviation=math.sqrt(dif/len(marks))
    print("The std deviation is: {:0.2f}".format(deviation))
    return deviation

def list_names(mean,deviation,marks,names):
    no1=mean-deviation
    fail=[]
    for i in range(len(marks)):
        if marks[i]<no1:
            fail.append(names[i])
    if len(fail) > 0:
        print('List of students who need to see an advisor:')
        for name in fail:
            print(name)
        
def main():
    filename=input('Enter the marks filename:\n')
    lines=student_marks(filename)
    marks=[]
    names=[]
    for line in lines:
        tmpL=line.split(',')
        names.append(tmpL[0])
        marks.append(int(tmpL[1]))
    average_mark=average(marks)
    deviation=std_dev(average_mark,marks)
    #list of students who need to see an advisor
    list_names(average_mark,deviation,marks,names)

main()