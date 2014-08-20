"""Question 1-Assignment 9
FRNHAN004
13 May 2014"""

import math
list1=[] #create a new list
sd=[]
student_advisor=[]
names=[]

file_name=input("Enter the marks filename:\n")

f=open(file_name, "r") #open file
lines=f.readlines() #read content,store as list of line
f.close() #close file

for i in range(len(lines)-1):
    lines[i]=lines[i][:-1] #take off"\n" & split lines into fields

for i in range (0, len (lines)): #scan through lines, if first field=student name
    entries = lines[i].split (',')
    list1.append(entries[1]) #add marks to list

sum1 = 0
for i in list1:
    sum1=float(i)+sum1
    
average=sum1/len(list1) #floating points

for i in range(0,len(list1)): #(x(0)-avrg)^2
    x=((int(list1[i])-average)**2)
    sd.append(x)

sum2=0 #get sum of sd
for i in sd:
    sum2=float(i)+sum2
    
sd_total=math.sqrt((sum2)/len(list1))#get standard deviation

for i in range(len(lines)): #split lines where the commma is
    lines[i] = lines[i].split(",")
    
name2=[] #create new list
mark2=[]

for i in range(len(lines)):
    name2.append(lines[i][0]) #get the first thing from list(names)
    mark2.append(lines[i][1])#get second thing from list(marks)

name=("\n").join(names)

print ("The average is:","%.2f"%average) #output
print ("The std deviation is:","%.2f"%sd_total) #output

risk = average - sd_total #if mark is 1sd below avrg

for i in range(len(mark2)):
    if float(mark2[i]) < float(risk):#must both be floats
        print("List of students who need to see an advisor:") #output
        break
    
for i in range(len(mark2)):
    if float(mark2[i]) < float(risk):
        print(name2[i])



    

