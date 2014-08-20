#Done by Guy Green
#Assignment 9 Question 1
#Analyzes students marks

import math


def analysis():
    """Works out Standard Deviation and mean and students who need to see an advisor"""
    filename=input("Enter the marks filename:\n")
    lines=[]
    marks=[]
    meanCalc=0
    SDCalc=0
    f=open(filename, "r")
    lines=f.readlines()
    f.close()
    for i in range(len(lines)-1):
        lines[i]=lines[i][:-1] #Taking away the last character
   
    for j in range(len(lines)):
        marks.append(lines[j].split(",")) #Seperating the marks and names
    
    for k in range(len(marks)):
        marks[k][1]=int(marks[k][1]) #Converting the marks to integers instead of strings
    
    for l in range (len(marks)):
        meanCalc+=marks[l][1] #Adding all the marks together
    
    mean=meanCalc/len(marks)
    
    for m in range (len(marks)):
            SDCalc+=(marks[m][1]-mean)**2  #Adding the square of the difference between the marks and mean
    
    SD=math.sqrt(SDCalc/len(marks))
    
    x="{0:.2f}".format(SD) #Rounding off to two decimal places
    y="{0:.2f}".format(mean)
    

    print("The average is:", y) #Printing What you guys actually want
    print("The std deviation is:",x)
    
    for n in range(len(marks)):
        if marks[n][1]<(mean-SD):
            print("List of students who need to see an advisor:") #Only printing this line if there is a student who needs to see an advisor
            break
        else:
            continue
    
    for m in range(len(marks)):
        if marks[m][1]<(mean-SD):
            print(marks[m][0]) #Printing Person's name if it is required
   

analysis()