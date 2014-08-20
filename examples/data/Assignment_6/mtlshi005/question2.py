#Shivaan Motilal
#21/04/14

import math


v1=input("Enter vector A:\n")
v1=v1.split(" ")

v2=input("Enter vector B:\n")
v2=v2.split(" ")

a,b,c,d,e,f=eval(v1[0]),eval(v2[0]),eval(v1[1]),eval(v2[1]),eval(v1[2]),eval(v2[2])

g,h,i=a+b,c+d,e+f                      #Adding and converting to string
ADD=[]
ADD.append(g)
ADD.append(h)
ADD.append(i)




#Full="A+B = [{0:1},{1:>2},{2:>2}]"

    
print("A+B = ",ADD,sep="")


#print(Full.format(g,h,i) )

j,k,l=a*b,c*d,e*f
MULT=j+k+l
print("A.B =",MULT)


m,n,o=abs(a)**2,abs(c)**2,abs(e)**2
MODA=m+n+o

MODA=math.sqrt(MODA)

print("|A| = {0:.2f}".format(MODA))




#print("|A| =",MODA)

p,q,r=abs(b)**2,abs(d)**2,abs(f)**2

MODB=p+q+r
MODB=math.sqrt(MODB)

print("|B| = {0:.2f}".format(MODB))


