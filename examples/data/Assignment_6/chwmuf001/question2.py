#Mufaro Chiwara - April 2014
import math
#get input
veca=input("Enter vector A:\n").split(" ")
vecb=input('Enter vector B:\n').split(" ")
add =[]

#convert arrays to ints
for i in range(3):
    veca[i]=eval(veca[i])
    vecb[i]=eval(vecb[i])
    
    

#add arrays    
for i in range (3):
    add.append(veca[i]+vecb[i])


multiply = (veca[0]*vecb[0])+(veca[1]*vecb[1])+(veca[2]*vecb[2])
A = math.sqrt((veca[0]**2)+(veca[1]**2)+(veca[2]**2))
B = math.sqrt((vecb[0]**2)+(vecb[1]**2)+(vecb[2]**2))

print("A+B =", add)
print("A.B =", multiply)
print("|A| =", '%.2f'%A)
print("|B| =", '%.2f'%B)

    

