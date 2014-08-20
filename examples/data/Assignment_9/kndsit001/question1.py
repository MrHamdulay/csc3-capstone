"""Program to analyse student marks
Sithasibanzi Kondleka
16 May 2014"""

import math

fname = input("Enter the marks filename:\n")
infile = open(fname, "r")
data = infile.readlines()
infile.close()

for i in range(len(data)):
    data[i] = data[i].replace("\n", "") #removing the space, replacing with empty string
    
average = 0 #start out with the average being zero
number = 0 #start out being zero
marks = [] #empty list to build up on

for j in range(len(data)):
    number+=1
    stop = data[j].index(",") #point before the marks
    average+= int(data[j][stop+1:])
    marks.append(data[j][stop+1:])

average = average/number

standard = 0.0

for i in marks:
    i = int(i)
    standard+= (i - average)*(i - average)
standard = math.sqrt(standard/number)


print("The average is: {0:0.2f}".format(average)) #rounding off
print("The std deviation is: {0:0.2f}".format(standard)) #rounding off

for x in range(len(data)): #if there ARE students who need to see an advisor
    if int(marks[x])<(average-standard):
        print("List of students who need to see an advisor:")
        break
    
for x in range(len(data)): #if there's no one who needs to see an advisor
    if int(marks[x])<(average-standard):
        stop = data[x].index(",")
        print(data[x][:stop])