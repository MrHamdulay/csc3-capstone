"""Assignment 9- Question 1: analysis of student marks
Duncan Saffy
May 12 2014"""
import math

filename= input("Enter the marks filename:\n")
file=open(filename,"r")
lines= file.readlines()
file.close()

count=0
mark=0
sum_mark=0
list_marks=[]

 
for line in lines:
    if len(lines)-1 == count:
        mark=eval(line[line.find(",")+1:])
    else:
        mark=eval(line[line.find(",")+1:])
    sum_mark+=mark
    list_marks.append(mark)
    count+=1
    

mean = sum_mark/count
total_sum=0

#solving for standard deviation
for i in range(count):
    x=list_marks[i-1]
    mean_sum=(x-mean)**2
    total_sum+=mean_sum

students=[]
student=""
# standard deviation formula
u= math.sqrt(total_sum/count)
poor_mark= mean-u
#Finding students with poor marks
for i in range(count):
    if list_marks[i]<poor_mark:
        student= lines[i][:lines[i].find(",")]
        students.append(student)            
    else:
        continue
        

print("The average is: {:0.2f}".format(mean))
print("The std deviation is: {:0.2f}".format(u))
if students!=[]:
    print("List of students who need to see an advisor:")
    for s in students:
        print(s)

