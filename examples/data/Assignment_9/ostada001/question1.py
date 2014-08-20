'''Advisor's List generator
determines which students should see a student advisor (from a list in a 
txt file)'''
import math
#initialising variables to store relavent values
fileName = input("Enter the marks filename:\n")
f = open(fileName,'r')
average = 0
stdDev = 0
advisorList = []

#stores each line of the text as separate list values
classList = f.readlines()

#Determine average
for i in range(len(classList)):
    
    average += eval(classList[i].split(',')[1])
    
average = round(average/len(classList),2)

#Determine standard deviation
for i in range(len(classList)):
    stdDev += (eval(classList[i].split(',')[1])-average)**2

stdDev = round(math.sqrt(stdDev/len(classList)),2)

#Determine whether a person's mark is one std deviation below average
for i in range(len(classList)):
    
    if (eval(classList[i].split(',')[1])) <= (average - stdDev) and len(classList)>1:
        advisorList.append(classList[i].split(',')[0])
#formats average variable to have a second zero for aesthetic purposes
if len(str(average).split('.')[1])!= 2:
    average = str(average)+"0"
#formats std Deviation variable to have a second zero for aesthetic purposes
if len(str(stdDev).split('.')[1]) != 2:
    stdDev = str(stdDev) +"0"
#print results    
print("The average is:",average)
print("The std deviation is:",stdDev)

if len(advisorList) >0:
    print("List of students who need to see an advisor:")
    for i in range(len(advisorList)):
        print(advisorList[i])
        
f.close()