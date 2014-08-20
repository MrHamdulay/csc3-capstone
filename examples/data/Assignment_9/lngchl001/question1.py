#program to print out the average, standard deviation and students who need to see an advisor
#14 May 2014
#By Chloe Longmore

import math

MarksDict={}
MarksList=[]
FileName=input('Enter the marks filename:\n')
f = open(FileName, 'r')
lines = f.readlines()
f.close()
Fail=[]

#chops off the new line character
for i in range (len (lines)-1):
    lines[i] = lines[i][:-1]

#get rid of extra quotes if any
for i in range (len (lines)):
    if lines[i] != "":
        if lines[i][0]== '"' or lines[i][0]== "'":
            lines[i] = lines[i][1:]
            if lines[i][-1] == '"' or lines[-1]== "'":
                lines[i] = lines[i][:-1]
#Get the marks
for i in range (len (lines)):
    Entries = lines[i].split (',')
    MarksDict[Entries[0]]=eval(Entries[1])
    Fail.append(Entries[0])
for key in MarksDict:
    MarksList.append(MarksDict[key])
    
#calculate average mark
AvMark = 0
StDev = 0
for i in MarksList:
    AvMark = AvMark + i
AvMark = AvMark/len(MarksList)    

#calculate standard deviation
for i in MarksList:
    StDev = StDev + (i - AvMark)**2

StDev = math.sqrt(StDev/len(MarksList))    
See = AvMark - StDev
AvMark ="{:.2f}".format(AvMark)
StDev ="{:.2f}".format(StDev)
print('The average is:' , AvMark)
print('The std deviation is:', StDev)

#check which students need to see the advisor
PrintedLine=False
for i in MarksDict.keys():
    if MarksDict[i] < See:
        PrintedLine=True
if PrintedLine:
    print('List of students who need to see an advisor:')
    for i in Fail:
        if MarksDict[i] < See:
            print(i)