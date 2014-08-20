'''Phillip Ruhesi
24/04/14
this program does basic vector calculations'''

import math                                                #imports math library inorder to use math functions
x=input('Enter vector A:\n')
vectorA=x.split()
y=input('Enter vector B:\n') 
vectorB=y.split()                                          #splits the contents of vector B to make a list
vectoradd=[]
vectordot=[]                                               #creates empty list
for i in range(3):
       vectoradd.append(eval(vectorA[i])+eval(vectorB[i])) #adds the first second and third values of vector A and vector B
print('A+B =',vectoradd)                                      

for j in range(3):   
       vectordot.append(eval(vectorA[j])*eval(vectorB[j])) #multiplys the individual x,y,z values of the vector together and adds the new vector to get the dot product
vectordot=round(vectordot[0]+vectordot[1]+vectordot[2],2)
print('A.B =',vectordot)       

A=round(math.sqrt((eval(vectorA[0])**2+eval(vectorA[1])**2+eval(vectorA[2])**2)),2) #Calculates the magnitude of vector A
#print('|A| =',A)
print("{0} = {1:.2f}".format('|A|',A))
B=round(math.sqrt((eval(vectorB[0])**2+eval(vectorB[1])**2+eval(vectorB[2])**2)),2)  #Calculates the magnitude of vector B
#print('|B| =',B)
print("{0} = {1:.2f}".format('|B|',B))