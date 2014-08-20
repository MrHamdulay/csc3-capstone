"""Calculating various operations between 2 vectors
By Daniel Newton
19/04/14"""

import math     #math function imported to use sqrt function


AList=[]
vectorA=input("Enter vector A:\n")  #Asks for input of first vector, and evaluates all 3 numbers, assigning them to variables.

for number in vectorA.split(' '):
    AList.append(number)

a1=eval(AList[0])
a2=eval(AList[1])
a3=eval(AList[2])


BList=[]
vectorB=input("Enter vector B:\n")  #Asks for input of second vector, and evaluates all 3 numbers, assigning them to variables.

for number in vectorB.split(' '):
    BList.append(number)
    
b1=eval(BList[0])
b2=eval(BList[1])
b3=eval(BList[2])


add1=a1+b1  #Calculates the addition of the vectors
add2=a2+b2
add3=a3+b3
print("A+B = [",add1,", ",add2,", ",add3,"]",sep='')    #prints the addition operation


multiplied=(a1*b1)+(a2*b2)+(a3*b3)  #Works out the multiplication of the vectors
print("A.B =",multiplied) #prints multiplication


AAbs=round(math.sqrt(a1**2+a2**2+a3**2),2)  #Works out |A|
if AAbs==0:     #Takes into account 0, as 0 always rounds to 0.0, no matter what round value inputted.
    print("|A| = 0.00")
else:
    print("|A| =",AAbs) #prints |A|


BAbs=round(math.sqrt(b1**2+b2**2+b3**2),2)  #Works out |B|
if BAbs==0:     #Takes into account 0, as 0 always rounds to 0.0, no matter what round value inputted.
    print("|B| = 0.00")
else:
    print("|B| =",BAbs) #prints |B|