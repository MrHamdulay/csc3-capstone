#CSC1015F
#ASSIGNMENT 9
#QUESTION 1
#WHTBAS001
#14/05/2014
import math

def avg(x):
    sumx = 0
    mu = 0 
    n = len(x)
    for i in x:
        sumx+=i[1]  #add each successive mark
    mu = (sumx/n)   #divide total marks by number of marks
    return mu

def stdev(x,mu):
    nvar = 0
    n = len(x)
    for i in x:
        nvar+= (i[1] - mu)**2   #adds each successive squared difference
    stdev = math.sqrt(nvar/n)   #takes root of total/number of entries
    return stdev

def student_advisor(x,mu,stdev):
    print("List of students who need to see an advisor:")
    minimum = mu - stdev    #minimum criteria to not go to student advisor
    for i in x:
        if i[1] < minimum:
            print(i[0]) #returns name whose corresponding name is less than requirement


#input section
marks = input("Enter the marks filename:\n")

#Import section
marklist = [] #empty list
f = open(marks, "r")  #opens the .txt file in read mode
for line in f:
    splitline = line.split(',')  #Splits each student and mark
    splitline[1] = eval(splitline[1])   #converts markstring into float/int
    marklist.append(splitline)    #adds each splitted line to array
f.close()

#output section
average = '{0:1.2f}'.format(avg(marklist))  #format avg. to 2 dec places
print("The average is:",average)
standard_deviation = '{0:1.2f}'.format(stdev(marklist,avg(marklist)))   #format stdev to 2 dec places
print("The std deviation is:",standard_deviation)
if stdev(marklist,avg(marklist)) != 0:
    student_advisor(marklist,avg(marklist),stdev(marklist,avg(marklist)))
else:
    print()