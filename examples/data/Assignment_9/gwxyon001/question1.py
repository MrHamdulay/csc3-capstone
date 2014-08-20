'''program to analyse student's marks from a file'''
import math

file= input("Enter the marks filename:\n")
f=open(file,'r')
file1=f.readlines()
f.close()
sum_marks=0 #create counter

for i in range(len(file1)):
    s= file1[i].split(',')
    x=int(s[-1])
    sum_marks+=x
    
mean= sum_marks/len(file1)

sum_minus=0

for j in range(len(file1)):
    s= file1[j].split(',')
    y=int(s[-1])    
    minus=(y-mean)**2
    sum_minus+=minus
    
std=math.sqrt(sum_minus/len(file1))

print("The average is:",'{0:1.2f}'.format(mean,2))
print("The std deviation is:",'{0:1.2f}'.format(std,2))
if len(file1)!=1:
    print("List of students who need to see an advisor:")
    for k in range(len(file1)):
        s= file1[k].split(',')
        x=int(s[-1])
        if x < (mean-std):
            print(s[0])
else:
    pass
    