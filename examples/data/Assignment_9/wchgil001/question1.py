#Gillian Wachira
#15/05/2014
#A program to know who needs to see a student advisor based on marks

import math
list_y=[]
dict_x={}
#read and close the file

filename=input("Enter the marks filename:\n")
infile=open(filename,"r")
lines=infile.readlines()
infile.close()
fail=[]

#removes new line characters
for i in range (len(lines)-1):
    lines[i]=lines[i][:-1]
    
#removing quotes that are not required
for i in range (len(lines)):
    if lines [i]!= "":
        if lines[i][0]=='"' or lines[i][0]=="'":
            lines[1]=lines[i][1:]
            if lines[i][-1]=='"' or lines[-1]=="'":
                lines[i]=lines[i][:-1]
                
#entering marks
for i in range (len(lines)):
    marks =lines[i].split(",")
    dict_x[marks[0]]=eval(marks[1])
    fail.append(marks[0])

for j in dict_x:
    list_y.append(dict_x[j])
    
StDev=0
AvMark=0
for i in list_y:
    AvMark=AvMark+i
AvMark=AvMark/len(list_y)

for i in list_y:
    StDev=StDev+(i-AvMark)**2
StDev=math.sqrt(StDev/len(list_y))
#find out who needs to see student advisor

difference=AvMark-StDev
AvMark= "{:.2f}".format (AvMark)
StDev= "{:.2f}".format (StDev)
print("The average is:", AvMark)
print("The std deviation is:",StDev)

k=False
for i in dict_x.keys():
    if dict_x[i]< difference:
        k=True
if k:
    print("List of students who need to see an advisor:")
    for i in fail:
        if dict_x[i]< difference:
            print(i)
