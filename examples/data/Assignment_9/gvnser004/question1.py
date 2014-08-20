
import math

names=[]
marks=[]

fname=input("Enter the marks filename:\n")

file=open(fname,"r")
count=0
for line in file:
    names.append(line[0:line.index(",")])
    marks.append(eval(line[line.index(",")+1:len(line)]))
    count+=1

file.close()

total=0
sum_marks=0
avg=0
sdv=0

for i in range(count):
    sum_marks+=marks[i]

avg=sum_marks/count

for i in range(count):
    total+=(marks[i]-avg)**2


sdv=math.sqrt(total/count)

print("The average is:","{:.2f}".format(avg))
print("The std deviation is:","{:.2f}".format(sdv))


flag=False

for i in range(count):
    diff=avg-sdv
    if(marks[i]<diff):
        
            flag=True

if(flag==True):
    print("List of students who need to see an advisor:")
    for i in range(count):
        if(marks[i]<diff):
                print(names[i]) 