'''add,multiply,and find norminals of 2 vectors
matshepo mashabela
24 april 2014'''

import math
#get vectors
va=[]

A=(input("Enter vector A:\n"))
A=A.split(" ")
for i in A:
    if i!=" ":
        num=eval(i)
        va.append(num)
vb=[]
B=(input("Enter vector B:\n"))
B=B.split(" ")
for i in B:
    if i!=" ":
        numb=eval(i)
        vb.append(numb)
#addition
a=va[0]+vb[0]
b=va[1]+vb[1] 
c=va[2]+vb[2]
print("A+B = [",a,", ",b,", ",c,"]",sep="")

#times
a=va[0]*vb[0]
b=va[1]*vb[1]
c=va[2]*vb[2]
added=a+b+c
print("A.B =", added)

#norminal for A
add=0
for i in va:
    d=i**2
    add+=d
    if i==va[0]:
        e=d   
    elif i==va[1]:
        f=d
    elif i==va[2]:
        g=d
        
square=math.sqrt(add)#add**(1/2)
square=round(square,2)
if square==0.0:
    print("|A| =","0.00")
else:    
    print("|A| =",square)

#norminal for B
add=0
for i in vb:
    d=i**2
    add+=d
    if i==vb[0]:
        e=d   
    elif i==vb[1]:
        f=d
    elif i==vb[2]:
        g=d
        
square=add**(1/2)
square=round(square,2)

if square==0.0:
    print("|B| =","0.00")
else:    
    print("|B| =",square)
   



   