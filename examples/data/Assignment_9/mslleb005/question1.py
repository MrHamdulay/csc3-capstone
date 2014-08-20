#program to print out a list of students who fall below one sd of a mean
#Lebogang masila
#16 may 2014

import math

#function to read the lines in a file
def readFile(filename):
    f = open(filename,'r')
    lines = f.readlines()
    f.close()
    newList = []
    #loop through the whole list and replace \n and create a new list
    for line in lines:
        newList.append(line.replace('\n','')) 
    return newList


def calcMean(marks): #a function to calculate mean using only marks
    count=0
    mean=0 
    for i in marks:
        count=count+1
        if count>0:
            mean=sum(marks)/count
    print("The average is: {:0.2f}".format(mean))
    return mean

def calcSd(mean,marks):  #a function to calculate standard deviation
    sd=0
    sum_dif=0
    dif=0    
    for i in marks:
        dif=(i-mean)**2
        sum_dif=dif+sum_dif #calculating variance
        sd=math.sqrt(sum_dif/len(marks)) #calculating sd
    print("The std deviation is: {:0.2f}".format(sd))
    return sd

def getListOfNames(mean,sd,marks,names): #a function to get the list of names of students who fall below one sd of a mean
    first=mean-sd
    failers = []
    for i in range(len(marks)):
        if marks[i]<first:
            failers.append(names[i])
    if len(failers) > 0:
        print('List of students who need to see an advisor:')
        for name in failers:
            print(name)
        
def main(): #a function which calls all the other functions
    filename = input('Enter the marks filename:\n')
    lines = readFile(filename)
    
    marks = []
    names = []
    
    for line in lines:
        x = line.split(',') #spliting list where there is a comma
        names.append(x[0]) #creating a new list of names
        marks.append(int(x[1])) #creating a new list of marks
    m = calcMean(marks) #mean
    sd=calcSd(m, marks) #standard deviation
    getListOfNames(m,sd,marks,names) #list of students who should see the student advisor

main()