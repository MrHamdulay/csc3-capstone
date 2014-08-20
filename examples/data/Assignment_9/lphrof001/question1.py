import math
filename=input("Enter the marks filename:\n")
f=open(filename,"r")
lines=f.readlines()
f.close()

for i in range (len (lines)-1):
    lines[i] = lines[i][:-1]
#this will split the name from the marks
for i in range(len(lines)):
    lines[i]=lines[i].split(",")

#this function will add all the marks    
def add(n):
    if n==0:
        return 0
    else:
        return int(lines[n-1][1])+add(n-1)
n=len(lines)

average=add(n)/n
print("The average is:","{0:.2f}".format(average))

#Calculation of the standard deviation
def S_Deviation(n):
    if n==0:
        return 0
    else:
        x=(int(lines[n-1][1]))-average
        y=x**2
        return y+S_Deviation(n-1)

Dev=S_Deviation(n)/n
Deviation=math.sqrt(Dev)
print("The std deviation is:","{0:.2f}".format(Deviation))
Advisor=average-Deviation
#Creating a list of students that have a mark lower than the 
Students=[]
for i in range(len(lines)):
    if int(lines[i][1])<Advisor:
        Students.append(lines[i][0]) #Finds the name of the student that needs to see a student advisor

if len(Students)>0:
    print("List of students who need to see an advisor:")
    for i in Students:
        print(i,end="\n")

