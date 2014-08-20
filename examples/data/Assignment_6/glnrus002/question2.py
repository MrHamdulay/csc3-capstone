#glnrus002
#Question 2
#22 April
#Write a program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
import math
def plus(vec_A,vec_B):
    add=[0,0,0]
    for i in range (3):#used extract then add pairs from different arrays
        one=eval(vec_A[i])
        two=eval(vec_B[i])
        add[i]=one+two#addition of respective values from different arrays
    print("A+B = "+str(add))
    
def product(vec_A,vec_B):
    mul=[0,0,0]
    for i in range (3):
        one=eval(vec_A[i])
        two=eval(vec_B[i])
        mul[i]=one*two#multiplies different values from different arrays in same position
    total=mul[0]+mul[1]+mul[2]#adds all individual multiplication
    print("A.B =",total)
    
def norm(vec_A,vec_B):#The norm of a single vector is the square root of the sum of the squares of the elements.    
    # first A
    prod=0
    for i in range (3):#squares values
        work=eval(vec_A[i])
        prod=prod+work**2
    prod=math.sqrt(prod)#finally, get squareroot
    print("|A| =","{:0,.2f}".format(round(prod,2))) 
    # Then B(repeat)
    prod=0
    for i in range (3):
        work=eval(vec_B[i])
        prod=prod+work**2
    prod=math.sqrt(prod)
    print("|B| =","{:0,.2f}".format(round(prod,2)))     
    
if __name__ =="__main__":
    vec_A=(input("Enter vector A:\n")).split(" ")
    vec_B=(input("Enter vector B:\n")).split(" ")
    plus(vec_A,vec_B)
    product(vec_A,vec_B)
    norm(vec_A,vec_B)