"""Vectors
Lubalethu Dube
23 April 2014"""
import math
def Mr_Vectors():
    #get the two vectors
    vect1=input("Enter vector A:\n")
    vect2=input("Enter vector B:\n")
    v1=vect1.split(" ")
    v2=vect2.split(" ")
    v3=[]
    j=0
    l=0
    v4=[]
    #put into different vectors
    for i in range(1):
        v3.append(v1)
        v3.append(v2)
    for i in range (2):
        j=0
        for i in range(3):
            k=(v3[l][j])
            j+=1
            v4.append(k)
        l+=1
        
    #change into numbers   
    u=eval(v4[1])
    v=eval(v4[2])
    w=eval(v4[3])
    x=eval(v4[4])
    y=eval(v4[5])
    z=eval(v4[0])
    
    #matrices calculations
    A=[(z+w),(u+x),(v+y)]
    B=((z*w)+(u*x)+(v*y))
    c=math.sqrt((z*z)+(u*u)+(v*v))
    d=math.sqrt((w*w)+(x*x)+(y*y))
    
    #return answers
    print("A+B =",A)
    print("A.B =",B)
    print("|A| =",("{0:.2f}").format(c))
    print("|B| =",("{0:.2f}").format(d))
    
Mr_Vectors()
    
    