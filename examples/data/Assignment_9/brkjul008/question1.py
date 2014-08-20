#student marks
#julia breakey
#13 may 2014

#get list of file data
file=input("Enter the marks filename:\n")
f=open(file, "r")
data=f.readlines()
f.close

#removing trailing new lines
for i in range(len(data)-1):
    data[i]=(data[i])[:-1]

#split list into sublists
for i in range(len(data)):
    data[i]=data[i].split(",")

#calculate mean    
summ=0
for i in range(len(data)):
    summ+=eval(data[i][1])
    
mean=summ/(len(data))

#calculate std deviation
import math
a=0
for i in range(len(data)):
    a+=(eval(data[i][1])-mean)**2

std=math.sqrt(a/len(data))

#print information
print("The average is:", "{0:.2f}".format(mean))
print("The std deviation is:", "{0:.2f}".format(std))


students=[]
for i in range(len(data)):
    if eval(data[i][1])<(mean-std):
        students.append(data[i][0])
    else:
        continue
if students!=[]:
    #calculate students who got less than mean - std dev
    print("List of students who need to see an advisor:")
    for i in students:
        print(i)