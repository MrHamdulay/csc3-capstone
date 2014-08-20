""" program to see which students need to see a student advisor
Jacqueline Blomendahl
13 May 2015"""
import math

filename=input("Enter the marks filename:\n")

file=open(filename, "r")
lists = file.readlines()
file.close()
 
marks=[] 
students=0
total=0
#finding position of comma, list of marks and total of marks
for i in lists:
    coma=i.find(",")
    marks.append(i[coma+1:])
    total+=eval(i[coma+1:])
    students+=1

mean=(total/students)

variance=0
for k in marks:
    k=float(k)
    variance+=(k-mean)**2
    
std_dev= (math.sqrt(variance/students))
    
print("The average is:", "{0:.2f}".format(mean))
print("The std deviation is:", "{0:.2f}".format(std_dev))

adv=[]
num=0
for f in lists:
    coma=f.find(",")
    if eval(f[coma+1:])< mean-std_dev:
        adv.append(f[:coma])
        num+=1
        
    else:
        continue
    
if num!=0:
    print("List of students who need to see an advisor:")
    for h in adv:
        print(h)
        