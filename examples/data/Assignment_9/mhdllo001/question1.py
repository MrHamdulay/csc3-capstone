import math
a=input("Enter the marks filename:\n")
filename=open(a,"r")
lines=filename.readlines()
names=[]
marks=[]
mean=0
for i in range(len(lines)):
    names.append(lines[i].split(",")[0])
    marks.append(eval(lines[i].split(",")[1].split("\n")[0]))
    mean=mean+marks[i]
mean=mean/len(lines)
standard=0
y=0
while(y<len(marks)):#Calculating standard deviation
    standard+=(marks[y]-mean)**2
    y=y+1
standard=math.sqrt(standard/len(marks))
print("The average is:","{:.2f}".format(mean))
print("The std deviation is:","{:.2f}".format(standard))
flag=False

for i in range(len(marks)):
    
    if(marks[i]<(mean-standard)):
        
        flag=True
if(flag):
    
    print("List of students who need to see an advisor:")
    
    for i in range(len(marks)):
        

        if(marks[i]<(mean-standard)):

            person=names[i]

            print(person)
filename.close()