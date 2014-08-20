""" A program to analyse students marks in a file
Sthabiso Andile Gazu
May 2014"""
import math
def readFile(filename):
    f = open(filename,'r') #open and read file
    lines = f.readlines()
    f.close()
    newList = []
    for line in lines:
        newList.append(line.replace('\n',''))
    return newList

def calcMean(marks):
    count=0
    mean=0 
    for i in marks:
        count=count+1
        if count>0:
            mean=sum(marks)/count
    print("The average is: {:0.2f}".format(mean))
    return mean
#check the marks
def calcSd(mean,marks):
    sd=0
    sum_dif=0
    dif=0    
    for i in marks:
        dif=(i-mean)**2
        sum_dif=dif+sum_dif
        sd=math.sqrt(sum_dif/len(marks))
    print("The std deviation is: {:0.2f}".format(sd))
    return sd
def getListOfNames(mean,sd,marks,names):
    first=mean-sd
    failures = []
    for i in range(len(marks)):
        if marks[i]<first:
            failures.append(names[i])
    if len(failures) > 0:
        print('List of students who need to see an advisor:')
        for name in failures:
            print(name)
        
def main():
    filename = input('Enter the marks filename:\n')
    lines = readFile(filename)
    
    marks = []
    names = []
    
    for line in lines:
        tmp = line.split(',')
        names.append(tmp[0])
        marks.append(int(tmp[1]))
    m = calcMean(marks)
    sd=calcSd(m, marks)
    getListOfNames(m,sd,marks,names) #list of students who should see the student advisor

main()