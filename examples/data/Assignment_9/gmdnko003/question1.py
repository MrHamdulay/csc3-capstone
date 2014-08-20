'''Program to analyse marks in file to determine which students need to see a student advisor
nkosi gumede
13 may 2014'''

import math
#test1.txt
x=input("Enter the marks filename:\n")


f=open(x, "r")
lines= f.readlines()
f.close()

#Remove '\n' from <lines> array
for i in range(len(lines)):
    lines[i]= lines[i][:-1]

#Isolate the numbers associated with each student
listed=[] #list of numbers
for i in range(len(lines)):
    number=""
    for j in lines[i]:
        if 48<=ord(j)<=57:
            number+=j
    listed.append(number)           

#1st work out the average (ave)
listed_sum=0
for i in listed:
    i=int(i)
    listed_sum+=i
ave=round(listed_sum/len(listed),2)
print("The average is:", '{0:0<5}'.format(ave))

#2ndly work out the standard deviation (stddev)
sdn=0
for i in listed:
    i=int(i)
    sdn+=(i-ave)**2
    add=sdn/len(listed)
std_dev=round(math.sqrt(add),2)
print("The std deviation is:", '{0:0<4}'.format(std_dev))

#Finally output the list of students needing to see a student advisor (mark<(ave-std_dev))
list2=[]
for i in range(len(listed)):
    listed[i]=int(listed[i])
    if listed[i]<(ave-std_dev):
        listed[i]=str(listed[i])
        names=(lines[i][:len(lines[i])-(len(listed[i])+1)])
        list2.append(names)
if list2!=[]:
    print("List of students who need to see an advisor:")
for i in list2:
    print(i)
    
