#program to ananlyse student marks
#Kayla Hendricks
#15/05/2014

import math
file=input("Enter the marks filename:\n")
test=open(file,"r")
line=test.readlines()
#start all variables as 0 or empty
total=0
count=0
mark=[] 
for i in line:
    #chop off newline symbol and append mark to empty list
    i=i[:-1]
    single=i.split(",")
    total+=int(single[1])
    count+=1
    mark.append(single[1])

test.close()

avr=total/count
print("The average is: {0:0.2f}".format(avr))
var=0
#working out varience
for i in mark:
    var+=((int(i)-avr)**2)
total_var=var/count
        
std_dev=math.sqrt(total_var)
print("The std deviation is:",round(std_dev,2))
names=open(file,"r")
names_list=[]
for line in names:
    #checking if mark is below one standard deviation of mean
    single=line.split(",")
    if int(single[1])<(avr-std_dev):
        #if so appending to empty list
        names_list.append(single[0])
names.close()

print("List of students who need to see an advisor:")
for name in names_list:
    print(name)