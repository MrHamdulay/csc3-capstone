"""
reneshan naidoo
ndxren013
15/05/2014
"""
from math import *

def main():
    
    markfile = input("Enter the marks filename:\n") #getting input froim the user
  
    marks = open(markfile, "r") #reading file
    
    sdic = {} #creating a dictionary
    listmarks = [] #creating array
    studentslist = [] #creating array
    
    for line in marks:
        student, mark = line.split(",") #spliting on every comma
        sdic[student] = mark[:len(mark)] #extracting the mark from the input
        listmarks.append(eval(mark[:len(mark)])) #populating created array with the substringed marks
        studentslist.append(student)
        
        

        totm = 0
    for x in sdic:
        totm = totm + eval(sdic.get(x)) #
        
    average = totm/len(sdic)    
    
    div = 0
    for i in sdic:
        number = eval(sdic.get(i))
        div = div + (number - average)**2
        
    stdDev = sqrt(div/(len(sdic)))
    stdDev1 = average - stdDev #end of std deviation calculation
    
    
    consults = []
    
    for mark in range(len(listmarks)):
        if listmarks[mark] < stdDev1: #evaluating the students marks against the std deviation
            consult = studentslist[mark]
            consults.append(consult)
    
    print("The average is: {0:0.2f}".format(average))#printing output
    print("The std deviation is: {0:0.2f}".format(stdDev)) #printing output
    
    
    for i in listmarks:
        if i < stdDev1:
            print("List of students who need to see an advisor:") #printing all the students who need to do the consultation
            break

    for s in consults:
        print(s)
    
            
    marks.close()
main()
