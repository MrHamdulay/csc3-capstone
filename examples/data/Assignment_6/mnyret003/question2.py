# A program to do basic vector calculations in 3 dimensions
# Retselisitsoe Monyake
# 23/04/2014

#Get the values from the user
A=input("Enter vector A:\n")
B=input("Enter vector B:\n")
Alist=A.split()
Blist=B.split()
#addition
addlist=[eval(Alist[0])+eval(Blist[0]),eval(Alist[1])+eval(Blist[1]),eval(Alist[2])+eval(Blist[2])]
#dot.product
product=eval(Alist[0])*eval(Blist[0])+eval(Alist[1])*eval(Blist[1])+eval(Alist[2])*eval(Blist[2])
    
# normalization
import math
normA= math.sqrt(eval(Alist[0])**2+eval(Alist[1])**2+eval(Alist[2])**2)
normB = math.sqrt(eval(Blist[0])**2+eval(Blist[1])**2+eval(Blist[2])**2)
print("A+B =",addlist)
print("A.B =",product)
print("|A| =",'{0:.2f}'.format(normA))
print("|B| =",'{0:.2f}'.format(normB))

