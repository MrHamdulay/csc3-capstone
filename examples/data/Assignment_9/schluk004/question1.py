#Program to perform operations on marklist
#Luke Schwartzkopff
#13 May 2014

import math
fname=input("Enter the marks filename:\n")
namelist=[]
marklist=[]
f=open(fname,"r")

for line in f:
    namelist.append(line.split(",")[0]) #append the part of the string before the comma to a namelist
    marklist.append(eval(line.split(",")[1])) #append the part after the comma to marklist and convert it to int

f.close()
total=0
sd=0

for i in marklist:#loop and sum total
    total+=i
    
mean=total/(len(marklist)) #calculate mean

for i in marklist: #1st part of sd calculation
    sd+=(i-mean)**2
    
sd=math.sqrt(sd/len(marklist)) #2nd part of sd calculation

print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(sd))
plist=False #check if anyone needs to see an advisor
for i in marklist:
    if i<(mean-sd):
        plist=True
        
if plist==True:
    print("List of students who need to see an advisor:") 
    for i in range(len(marklist)): #check which marks are 1 sd below mean and print the corresponding names
        if marklist[i]<(mean-sd):
            print(namelist[i])

    
    