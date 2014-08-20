'''Program to do basic vector calculations in 3D
Mahnoor Ahmed
23 April 2014'''

import math

vecA=input("Enter vector A:\n")
vecB=input("Enter vector B:\n")
comblist=[]
vecA=vecA.split(" ")                                         #makes vector A a list of its components
vecB=vecB.split(" ")
comblist.append(vecA)                                        #adds the list of vectors to an empty list
comblist.append(vecB)

#Adding vectors
x=eval(comblist[0][0])+eval(comblist[1][0])                  #retrieves vectors corresponding to the possitions to add them
y=eval(comblist[0][1])+eval(comblist[1][1])
z=eval(comblist[0][2])+eval(comblist[1][2])
print("A+B ","= ","[",x,", ",y,", ",z,"]",sep="")            

#Dot product of vectors
a=eval(comblist[0][0])*eval(comblist[1][0])                  #multiplies corresponding vectors together
b=eval(comblist[0][1])*eval(comblist[1][1])
c=eval(comblist[0][2])*eval(comblist[1][2])
print("A.B ","= ",(a+b+c),sep="")

#|A|
absA=math.sqrt(((eval(comblist[0][0]))**2)+((eval(comblist[0][1]))**2)+((eval(comblist[0][2]))**2))       
absA="{0:1.2f}".format(absA)
print("|A| ","= ",absA,sep="")    

#|B|
absB=math.sqrt(((eval(comblist[1][0]))**2)+((eval(comblist[1][1]))**2)+((eval(comblist[1][2]))**2))
absB="{0:1.2f}".format(absB)
print("|B| ","= ",absB,sep="")                                 #retrieves components of the vector, squares it, adds the squared parts and then square roots it
