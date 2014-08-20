"""Ryan Kopping
13 May 2014
program to find students who need to see student advisor"""
import math
#get input and open the file and read
file=input("Enter the marks filename:\n")
f=open(file,"r")
marks = f.readlines()
marks[-1]+=("\n")
f.close
linesCounter=0
marksCounter=0
standardDevSq =0
#delete \n from the last characters
for i in range(len(marks)):
    marks[i]=marks[i][:-1]
    
    commaPosition=marks[i].find(",")
    marksCounter += (eval(marks[i][commaPosition+1:]))
    linesCounter+=1
#work out and print the average     
average = marksCounter/linesCounter
print("The average is:","%0.2f"%average)
#split the line on a comma to get the marks and work out standard deviaiton
for i in range(len(marks)):
    commaPosition=marks[i].find(",")
    standardDevSq  += ((eval(marks[i][commaPosition+1:])-average)**2)
standardDevSq = (math.sqrt(standardDevSq/linesCounter))
print("The std deviation is:","%0.2f"%standardDevSq)
    
#if the marks is less then one standard deviation from the mean, add them to the list
advisor=[]
for i in range(len(marks)):
    commaPosition=marks[i].find(",")
    if(eval(marks[i][commaPosition+1:])<(average-standardDevSq)):
        advisor.append(marks[i][:commaPosition])
        
#print out the list of students tp see the advisor         
if(len(advisor)>=1):
    print("List of students who need to see an advisor:")
    for i in range (len(advisor)):
        commaPosition=marks[i].find(",")
        print(advisor[i])
    
