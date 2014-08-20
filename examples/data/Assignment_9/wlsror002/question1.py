"""Assignment 9 Question 1
10 May 2014
Rory Welsh, Who Needs to See Advisor"""
import math
MarksDict={}
MarksList=[]
FileName=input('Enter the marks filename:\n')
f = open(FileName, 'r')
lines = f.readlines()
f.close()
Fail=[]

#Chops off the new line character
for i in range (len (lines)-1):
    lines[i] = lines[i][:-1]

#Get rid of extra quotes if any
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

AvMark = 0
StDev = 0
for i in MarksList:
    AvMark = AvMark + i
AvMark = AvMark/len(MarksList) #Mean value   

for i in MarksList:
    StDev = StDev + (i - AvMark)**2

StDev = math.sqrt(StDev/len(MarksList)) #Standard deviation calulation   
See = AvMark - StDev
AvMark ="{:.2f}".format(AvMark)
StDev ="{:.2f}".format(StDev)
print('The average is:' , AvMark)
print('The std deviation is:', StDev)


PrintedLine=False
for i in MarksDict.keys():
    if MarksDict[i] < See:
        PrintedLine=True
if PrintedLine: #Only prints this line if it is needed
    print('List of students who need to see an advisor:')
    for i in Fail:
        if MarksDict[i] < See:
            print(i)