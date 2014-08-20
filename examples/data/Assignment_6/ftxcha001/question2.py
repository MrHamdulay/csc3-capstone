#Chantel Foot
#Question 2, Assignment 6


import math #to use things such as round, math.sqrt ... 

vector_listA = input("Enter vector A:\n") #get the list
vector_listB = input("Enter vector B:\n") #see above

vector_a= vector_listA.split(" ") #split the list into each string at each space.
vector_b= vector_listB.split(" ") #do the same for input values in vector b 

a1= eval(vector_a[0]) #eval each string to use in calculations
a2= eval(vector_a[1])
a3= eval(vector_a[2])
b1= eval(vector_b[0])
b2= eval(vector_b[1])
b3= eval(vector_b[2])

c=math.sqrt((a1*a1)+(a2*a2)+(a3*a3))
d=math.sqrt((b1*b1)+(b2*b2)+(b3*b3))

print("A+B ="," [",(a1+b1),", ",(a2+b2),", ",(a3+b3),"]",sep="") #print with neccessary calculation
print("A.B =",(a1*b1)+(a2*b2)+(a3*b3))
print("|A| =", "{:.2f}".format(c)) #format to two decimal places (0 case)
print("|B| =", "{:.2f}".format(d)) 

