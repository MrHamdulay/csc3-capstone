# Program analyses student marks read from a file and determines which students need to see an advidor
# Wandile Lesejane
# 14 May 2014

# open the file
file=input("Enter the marks filename:\n")
f=open(file,"r")
lines=f.readlines()
f.close()
lis=[]

# remove the new line
for i in range(len(lines)):
    lines[i]=lines[i][:-1]

#list of marks
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j]==',':
            lis.append(lines[i][j+1:])
       
    for i in range(len(lis)):
        lis[i]=int(lis[i])    
        
total=0
#average mean
for i in range(len(lis)):
    total+=lis[i]
mean=total/len(lis)
print("The average is:","%.2f" %(mean))

#standard deviation
import math
sd=0
for i in range(len(lis)):
    sd+=(lis[i]-mean)**2
sdv=math.sqrt(sd/len(lis))

#list of students
print("The std deviation is:","%.2f"%(sdv))
 
if sdv>0:
    print("List of students who need to see an advisor:")
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j]==',':
                if lis[i]<(mean-sdv):
                    print(lines[i][:j])
    