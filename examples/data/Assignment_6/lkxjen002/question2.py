#A program to do basic vector calculations
#created by:Jenna Lake
#date: 25/4/2014

import math
def vector(): 
    
    list1=[]
    a=input("Enter vector A:\n")
    x,y,z=a.split(" ")
    list1.append(x)
    list1.append(y)
    list1.append(z)
    
    b=input("Enter vector B:\n")
    list2=[]
    u,v,w=b.split(" ")
    list2.append(u)
    list2.append(v)
    list2.append(w)    

    
#def addition():        
    list_add=[]
    pos1=eval(list1[0])+eval(list2[0])
    pos2=eval(list1[1])+eval(list2[1])
    pos3=eval(list1[2])+eval(list2[2])
    print("A+B = [",pos1, ", ",pos2,", ",pos3, "]", sep="")


#def dot_product():
    pos1a=eval(list1[0])*eval(list2[0]) 
    pos2a=eval(list1[1])*eval(list2[1])
    pos3a=eval(list1[2])*eval(list2[2])
    print("A.B = ", pos1a+pos2a+pos3a, sep="")


#def norm_A():
    sqx=eval(list1[0])**2
    sqy=eval(list1[1])**2
    sqz=eval(list1[2])**2
    sumA=math.sqrt(sqx + sqy + sqz)
    sumA1=(round(sumA*100)/100)
    if sumA1==0.0:
        print("|A| = ",sumA1, "0", sep="") #ensures than answer will always be to two decimal places by dealing with the one execption
    else:
        print("|A| = ", sumA1, sep="")

    
#def norm_B():
    squ=eval(list2[0])**2
    sqv=eval(list2[1])**2
    sqw=eval(list2[2])**2
    sumB=math.sqrt(squ + sqv + sqw)
    sumB1=(round(sumB*100)/100)     # round to two decimal places
    if sumB1==0.0:
            print("|B| = ",sumB1, "0", sep="")
    else:
        print("|B| = ", sumB1, sep="") 
vector()
    
