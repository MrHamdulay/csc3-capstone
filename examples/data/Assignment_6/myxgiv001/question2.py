
import math
    #add vectors
def add(x,y):
    plus=[]
    for i in range(3):
        plus.append(x[i]+y[i])
    return plus
    
#multiply vectors
def times(x,y):
    multply=0
    for i in range(3):
        multply=multply+(x[i]*y[i])
    return multply
#find length of vector
def modulus(x):
    vector=math.sqrt(x[0]**2 + x[1]**2 +x[2]**2)
    return vector
x=input("Enter vector A:\n")
y=input("Enter vector B:\n")

x=x.split()
y=y.split()
for i in range(3):
    x[i]=eval(x[i])
    y[i]=eval(y[i])
print ("A+B =",add(x,y))
print ("A.B =",times(x,y))
print ("|A| =","{:.2f}".format(modulus(x)))
print ("|B| =","{:.2f}".format(modulus(y)))
    
    