"""Program to check if marks
By Tinashe Choga
12/05/2014"""
import math 

#openning the file
filename=input("Enter the marks filename:\n")
file=open(filename,"r")
lines=file.read()
file.close()

#splitting the string into a 2D array/list
lin3=lines.split('\n')
line=lin3[:len(lin3)-1]

list2=[]
for i in line:
    m=i.split(",")
    list2.append(m)
    
"""placing the marks in their own list for easy mathematical manipulation"""
list=[]
for k in list2:
    list.append(int(k[1]))
sum=0
#finding the sum
for j in list:
    sum+=j
#the average
average=sum/len(list)
standard_d=0

#standard deviation
for s in list:
    standard_d+=(s-average)**2
st=math.sqrt(standard_d/len(list))
minimum=average-st

print("The average is: {0:0.2f}".format(average))
print("The std deviation is: {0:0.2f}".format(st))


#evaluating and printing
for check in list2:
    if int(check[1])< minimum:
        print("List of students who need to see an advisor:")
        break
for check in list2:
     if int(check[1])< minimum:
         print(check[0])