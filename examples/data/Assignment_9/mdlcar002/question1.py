"""15 May 2014
MDLCAR002
Assignment 9 Question 1
Program to analyse student marks from a file and determine which students need to see a student advisor"""


import math
def main():
    totalmarks=0
    students=0
    stdDevSum=0
    names_marks=[]
    
    filename=input("Enter the marks filename:\n")
    f=open(filename,"r") # file will only be read
    for line in f:
        Line=line.split(",") #splits the string
        names_marks.append(Line)
        students+=1 #counts the number of student, since there is a student name on each line 
        totalmarks+=int(Line[1]) #adds on each mark
        
    f.close()
    average=totalmarks/students 
    for i in range(students):
        stdDevSum+=(int(names_marks[i][1])-average)**2
        
    stdDev=math.sqrt((stdDevSum/students)) #calculating the standard deviation
    
    print(("The average is: {0:"+str((len((str(average))[0:2])+1))+".2f}").format(average))
    print(("The std deviation is: {0:"+ str((len((str(stdDev))[0:2])+1))+".2f}").format(stdDev))
    advisor=[] #this list will store the names of students who need to see the advisor
    testing=""
    for i in range(students):
        if int(names_marks[i][1])<(average-stdDev): #compares each marks to one less standard deviation than the mean
            advisor.append(names_marks[i][0]) #those which are less get added to the advisor list
            testing=names_marks[i][0]
    if testing!="":
        print("List of students who need to see an advisor:")
        for i in range(len(advisor)): #loops through the list and prints out students names
            print(advisor[i])
            
    
main()    
    
    
    
    
    