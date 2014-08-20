"""Yonela Ford
Programme to manipulate vectors
23 April 2014"""

# get input
vector_A=input("Enter vector A:\n")
vector_B=input("Enter vector B:\n")
#create lists
x=vector_A.split()
y=vector_B.split()
import math
#add vectors
def add():
    new_vector=[]
    for i in range (len(x)):
        for j in range (len(y)):
            
            if i==j:
                b=eval(x[i])+eval(y[i])
                new_vector.append(b)
    print("A+B =", new_vector)
#multiply vectors
def multiply():    
    new_vector=[]
    for i in range (len(x)):
        for j in range (len(y)):
            
            if i==j:
                b=eval(x[i])*eval(y[i])
                new_vector.append(b)
    d=0
    for a in new_vector:
        d+=a
    print ("A.B =", d)
#norm vector for A
def squareroot_A():
    newest=[]
    for i in x:
        f=eval(i)**2
        newest.append(f)
    r=0
    for p in newest:
        r+=p
    print ("|A| =","{0:.2f}".format(math.sqrt(r)))

# norm vector for B
def squareroot_B():
    newest=[]
    for i in y:
        f=eval(i)**2
        newest.append(f)
    r=0
    for p in newest:
        r+=p
    print ("|B| =","{0:.2f}".format(math.sqrt(r)))
add()
multiply()
squareroot_A()
squareroot_B()

    
        

    
    

                
            