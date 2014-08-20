#program to analyse marks of students in terms of deviation
#mlsomp001
#16 may 2014


import math

file= input("Enter the marks filename:\n")
f=open(file,'r')
file1=f.readlines()
f.close()
sum1=0 #begining of counter

for i in range(len(file1)):
    s= file1[i].split(',')
    x=int(s[-1])
    sum1+=x
    
mean= sum1/len(file1)#calculation of the mean

sum2=0

for j in range(len(file1)):
    s= file1[j].split(',')
    y=int(s[-1])    
    minus=(y-mean)**2
    sum2+=minus
    
standard_dev=math.sqrt(sum2/len(file1))#calculating the standard deviation

print("The average is:",'{0:1.2f}'.format(mean,2))
print("The std deviation is:",'{0:1.2f}'.format(standard_dev,2))
if len(file1)!=1:
    print("List of students who need to see an advisor:")
    for k in range(len(file1)):
        s= file1[k].split(',')
        x=int(s[-1])
        if x < (mean-standard_dev):
            print(s[0])
else:  #final results
    pass
    