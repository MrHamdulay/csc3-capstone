#Shivaan Motilal


import math

#Read contents from file
file=input("Enter the marks filename:\n")
f=open(file,"r")
data=f.readlines()


#Create a list or dict to store values
students=[]
for l in range(0,len(data)):
 
 if l!=len(data):
  data[l]=data[l][:-1]
 
 
 pair=data[l].split(",")
 students.append(pair)

count=0
sumt=0
for pair in students:
 pair[1]=eval(pair[1])
 count+=1
 sumt+=pair[1]        

#Calculate average as total sum over total num
ave=sumt/count


#calculate standard dev using average

acc=0
for pair in students:
 term=(pair[1]-ave)**2
 acc+=term
sd=math.sqrt(acc/count) 

#if value assoc with student less than (average-sdev), then print name






"""print ot output"""


print("The average is: {0:.2f}".format(ave))
print("The std deviation is: {0:.2f}".format(sd))


count=1
for pair in students:
 if pair[1]<(ave-sd):
  if count==1:
   print("List of students who need to see an advisor:")
   count+=1
  print(pair[0])
 



