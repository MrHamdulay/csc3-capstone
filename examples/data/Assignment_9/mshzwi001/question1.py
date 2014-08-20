# a Python program to analyse student marks read in from a file and determine which students need to see a student advisor
# mashau zwivhuya
# 12 may 2014
import math
#getting input
file=input("Enter the marks filename:\n")
#opening the file
f=open(file,"r")
#reading the file
lines=f.readlines()
#closing the file
f.close()
list1=[]
list2=[]
#looping through the document and appending to list
for i in lines:
    if i[-1]=="n":
        i=i[:-2]
    list1.append(i)
# removing the new line character from strings
for i in range(len(list1)-1):
    x=list1[i]
    y=x[0:-1]
    list2.append(y)
list2.append(list1[-1])
names=[]
marks=[]
for i in list2:
    x=i.split(",")
    marks.append(x[1]) 
    names.append(x[0])
    
# calculating the average
summ=0
for i in marks:
    summ=summ+int(i)
average=summ/(len(marks))
#printing average
print("The average is:","%1.2f " % average)
# calculating standard deviation
std=0
for i in marks:
    x=(int(i)-average)**2
    std=std+x
std_dev=math.sqrt(std/len(marks))
std_dev_below=average-std_dev
# printing out students who get marks below one standard deviation
print("The std deviation is:","%1.2f " % std_dev)
#condition for printing out students
k=False
for i in marks:
    if int(i)<std_dev_below:
        k=True

if k:
    print("List of students who need to see an advisor:")
for i in marks:
    if int(i)<std_dev_below:
        y=marks.index(i)
        print(names[y])

