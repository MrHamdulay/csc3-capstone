#Aniq Hartle
#12/05/2014
#open file of marks and output list of students who need to see advisor based on std.deviation from mean

import math

uiFile = input("Enter the marks filename:\n")                 #take in input

f = open (uiFile, "r")     #open file to read
lines = f.readlines()      #create array of lines
f.close ()                 #close file

marks = []                 #create array for marks
advisor = []
for line in lines:                            #update marks array with marks
    marks.append(eval(line.split(",")[1]))

mean = sum(marks)/float(len(marks))                            #calculate mean
sd = math.sqrt(sum((x-mean)**2 for x in marks)/len(marks))     #calculate standard deviation
print("The average is:","{0:.2f}".format(mean))
print("The std deviation is:","{0:.2f}".format(sd))
for line in lines:                                             #if mark is one stdev less than mean print name
    if eval(line.split(",")[1])<(mean-sd):
        advisor.append(line.split(",")[0])
if len(advisor)>0:
    print("List of students who need to see an advisor:")
    for i in advisor:                                            
        print(i)    