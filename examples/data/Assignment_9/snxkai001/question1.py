#kairav soni
#15/5/14
#Q1 Ass9
import math

fname=input("Enter the marks filename:\n")
f=open(fname,"r")
lines=f.readlines()
f.close()

for i in range (len(lines)):
       lines[i]=lines[i][:-1]
       
for i in range(len(lines)):
       lines[i] = lines[i].split(",")
#print(doc[i]) 

add=0   
for i in range(len(lines)):
       add += eval(lines[i][1])
       
mean=str(round(add/(len(lines)),2))
av_string=mean.split(".")
print("The average is: {0}.{1:0<2}".format(av_string[0],av_string[1]))

var=0
for i in range(len(lines)):
       var += ((eval(lines[i][1]) - eval(mean)) ** 2)
       
stddev=str(round(math.sqrt(var/(len(lines))),2))
list1=stddev.split(".")
print("The std deviation is: {0}.{1:0<2}".format(list1[0],list1[1]))

fail=eval(mean)-eval(stddev)
list2=[]
for i in range(len(lines)):
       if eval(lines[i][1])<(fail):
              list2.append(lines[i][0])
              
if len(list2)>0:
       print("List of students who need to see an advisor:")
if len(list2)>0:
       for names in list2:
              print(names)