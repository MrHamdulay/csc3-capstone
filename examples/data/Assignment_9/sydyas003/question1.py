#Yaseen Sayed Ismail
#SYDYAS003
#11/05/2014
#Program to analyse student marks read in from a file and determine which students need to see a student advisor.

import math#Import math library for square root function

filename=input("Enter the marks filename:\n")#Receives file name from user
f = open(filename,"r")#Reads file specified by user
lines=f.readlines()#Reads each line as a new element in a list,lines
marks=[]#Define list to store marks
names=[]#Define list to store names
mean=0#Define variable to store mean value

#Loops through list of lines and populates marks and names lists by splitting each line at the comma
#Converts marks elements to integers and adds them to mean, producing the sum of all marks
for i in range(len(lines)):
    marks.append(lines[i].split(',')[1].split("\n")[0])
    names.append(lines[i].split(',')[0])
    marks[i]=int(marks[i])
    mean+=marks[i]

mean=mean/len(marks)#Mean, or sum is divided by the number of marks to calculate the average
sd=0#Define variable to store standard deviation

#Loops through marks list and adds the square of the difference between each mark and the mean to sd
for i in range(len(marks)):
    sd+=(marks[i]-mean)**2

sd=math.sqrt(sd/len(marks))#Calculates standard deviation by taking the square root of sd divided by the number of marks

print("The average is:","{:.2f}".format(mean))#Displays the average to 2 decimal places
print("The std deviation is:","{:.2f}".format(sd))#Displays the standard deviation to 2 decimal places

flag=False#Define flag to indicate whether any student needs to see the advisor

#Sets flag, true if any student needs an advisor and false if no students need an advisor
for i in range(len(marks)):
    if(marks[i]<(mean-sd)):
        flag=True

#If there is/are student(s) who need to see advisors, displays the students who need to see advisors
if(flag):
    print("List of students who need to see an advisor:")
    for i in range(len(marks)):
        if(marks[i]<(mean-sd)):
            print(names[i])
