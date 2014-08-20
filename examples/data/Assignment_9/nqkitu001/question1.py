"""Assignment 9 
Question1 
Itumeleng Nqoko
Thursday 15th MAy 2014"""
#program to read 
import math
filename=input("Enter the marks filename:\n")
f=open(filename,"r")
lines=f.read().replace("\n",",").split(",")
naughty=""
mean=0
count=0
for i in range(1,len(lines),2):
    count+=eval(lines[i])
mean=count//(len(lines)//2)
varlis=[]
names=""
for j in range(1,len(lines),2):
    varlis.append((eval(lines[j])-mean)**2)
var=0
for k in varlis:
    var+=k
variance=var//(len(lines)//2)

sd=(math.sqrt(variance))
sdf = "{0:.2f}".format(sd)
deviation=mean-eval(sdf)
for i in range(1,len(lines),2):
    if eval(lines[i])<deviation:
        naughty+=lines[i-1]
f.close()     
print("The average is:","{0:.2f}".format(mean))
print("The std deviation is:",sdf)
print("List of students who need to see an advisor:")
print(naughty)

            
        
    

