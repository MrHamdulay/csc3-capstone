import math

def get_vector(a):
    y=[]
    print("Enter vector ", a, ":", sep="")
    
    b=input()
    b=b.split(" ")
    for i in b:
        y.append(eval(i))
    return y

def add_vector(a, b):
    y=[]
    for i in range(3):
        y.append(a[i]+b[i])
    return y

def dot_product(a, b):
    y=0
    for i in range(3):
        y+=a[i]*b[i]
    return y

def vector_norm(a):
    y=0.00
    for i in range(3):
        y+=a[i]**2
    if y==0:
        y="0.00"
    elif y!=0:
        y=(round(math.sqrt(y), 2))
    return y

def vector_final():
    z=get_vector("A")
    q=get_vector("B")
    print("A+B =", add_vector(z, q))
    print("A.B =", dot_product(z, q))
    print("|A| =", vector_norm(z))
    print("|B| =", vector_norm(q))
    
vector_final()