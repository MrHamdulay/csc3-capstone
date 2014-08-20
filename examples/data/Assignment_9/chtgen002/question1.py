"""CHTGEN002
12/05/14
Standard Deviation Marks
"""
import math #math functions enabled

markfile=input("Enter the marks filename:\n") #opening of file
f=open(markfile,"r")
data=f.readlines()

marks=[] 
sum=0
sdsum=0
names=[]

for i in range (len(data)): #remove marks to another list 
    y=data[i]
    pos=y.index(",")
    m=eval(y[pos+1:])
    marks.append(m)

for j in range (len(marks)): #sum of marks
    sum=sum+marks[j]

mean=sum/(len(marks)) #mean calculation 

for k in range (len(marks)): #sum of the square of every mark minus mean
    sdsum=sdsum+(((marks[k])-mean)**2) 

dev=(sdsum/(len(marks)))**(0.5) #std deviation calculation
minusonesd=mean-dev #min mark ie: mean minus one std deviation

first=""


for l in range (len(data)): #print out names of people
    if (marks[l]<minusonesd):
        z=data[l]
        stpos=z.index(",")
        nm=z[:(stpos)]
        names.append(nm)

listnames="\n".join(names)

print("The average is:", "%.2f" % mean)
print("The std deviation is:", "%.2f" % dev)
if (len(names)>0):
    print("List of students who need to see an advisor:\n",listnames,sep="")



f.close()
    
    

