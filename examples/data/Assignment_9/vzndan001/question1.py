"""files: marks below one standard deviation
danica van der zandt
11 may 2014"""

import math

filename=input("Enter the marks filename:\n")
#read in the files to get marks
f=open(filename,"r")
students=(f.readlines())
f.close()

#get all the marks for calculation
marks=[]
temp_list=[]
for student in students:
    temp_list.append(student[:len(student)-1])
    
for amark in temp_list:
    tmp = amark.split(",")
    marks.append(tmp[1])
    
#getting the average
total=0
N=len(marks)
for i in marks:
    total+=int(i)
    
average=total/N
average="%2.2f" % average

#standard deviation of the mean
sttotal=0
for j in marks:
    st=(float(j)-float(average))**2
    sttotal+=st
    
stdev="%2.2f" % math.sqrt(sttotal/N)



print("The average is:",average)
print("The std deviation is:",stdev)

#one less than std deviation
oneless_stddev=float(average) - float(stdev)
oneless_stddev="%2.2f" % oneless_stddev

#checking if student needs advice       
temp_advice=[]
for student in students:
    temp = student.split(",")
    temp = temp[1]
    temp = float(temp[:len(temp)-1])
    if temp < float(oneless_stddev):
        temp_advice.append(student)
    else:
        continue

#printing students who need advice
list_advice2=[]
if stdev!="0.00":
    print("List of students who need to see an advisor:\n",end="")
    for person in temp_advice:
        list_advice=person.split(",")
        list_advice=list_advice[0]
        list_advice2.append(list_advice)
        
    for name in list_advice2:    
        print(name)
    
    