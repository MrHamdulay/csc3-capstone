# A program to do basic vector calculations in 3 dimensions
#Sandisha Budhal
#BDHSAN003

VECT_A=input("Enter vector A:\n") #ask user to input the vectors a and b
VECT_B=input("Enter vector B:\n")

VECT_Alist=VECT_A.split()
VECT_Blist=VECT_B.split()

sum_list=[eval(VECT_Alist[0])+eval(VECT_Blist[0]),eval(VECT_Alist[1])+eval(VECT_Blist[1]),eval(VECT_Alist[2])+eval(VECT_Blist[2])]

prodct=eval(VECT_Alist[0])*eval(VECT_Blist[0])+eval(VECT_Alist[1])*eval(VECT_Blist[1])+eval(VECT_Alist[2])*eval(VECT_Blist[2])
    
#import math library in order to use squareroot function
import math
A= math.sqrt(eval(VECT_Alist[0])**2+eval(VECT_Alist[1])**2+eval(VECT_Alist[2])**2)
B = math.sqrt(eval(VECT_Blist[0])**2+eval(VECT_Blist[1])**2+eval(VECT_Blist[2])**2)

print("A+B =",sum_list)
print("A.B =",prodct)

print("|A| =",'{0:.2f}'.format(A))
print("|B| =",'{0:.2f}'.format(B))

