'''Question1 -Assignment 9- calculating avg and std deviation frm list in file
GVNPRI022-Prinesan Govender
13 May 2014'''
import math
filename= input("Enter the marks filename:\n")

f= open(filename,"r")
listData= f.readlines()
f.close()
oneLine=[]
sumOfMarks=0
sumSquare=0
for x in range(len(listData)):#creating list
    oneLine.append(listData[x].split(","))
    

for i in range(len(listData)): #calculating sum of marks
    sumOfMarks= eval(oneLine[i][1])+sumOfMarks
    
avg= sumOfMarks/len(listData) #calculating average

for j in range(len(listData)): #loop to find the sum of the terms that are squared in order to find standard deviation
    term= (eval(oneLine[j][1])-avg)**2
    sumSquare= term+sumSquare


std_deviation=  math.sqrt(sumSquare/len(listData)) #calculating standard deviation

avg= round(avg,2)
std_deviation= round(std_deviation,2)
#formatting output
print_avg= "{0:0.2f}".format(avg)
print_std_deviation= "{0:0.2f}".format(std_deviation) 
print("The average is:",print_avg)
print("The std deviation is:",print_std_deviation)
if(std_deviation>0): #printing list of students who need to see an advisor
    
    print("List of students who need to see an advisor:")
    for k in range(len(listData)):
        if (eval(oneLine[k][1])<avg-std_deviation):
            print(oneLine[k][0])
    