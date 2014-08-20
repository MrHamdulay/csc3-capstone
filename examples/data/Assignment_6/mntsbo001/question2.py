def main():
    # Making the vectors and its components
    A = input("Enter vector A:\n")
    A = A.split()
    a = eval(A[0])
    b = eval(A[1])
    c = eval(A[2])
    A = [a,b,c]
    B = input("Enter vector B:\n")
    B = B.split()
    d = eval(B[0])
    e = eval(B[1])
    f = eval(B[2])
    B = [d,e,f]
    #The sum of the vectors
    print("A+B = ["+str(a+d)+",",str(b+e)+",",str(c+f)+']')
    #The dot product
    print("A.B =",(a*d)+(b*e)+(c*f))
    #The magnitude of each vector
    import math
    t=round(math.sqrt(a**2+b**2+c**2),2)
    u=round(math.sqrt(d**2+e**2+f**2),2)
    print("|A| =","{0:0<4}".format(t))
    print("|B| =","{0:0<4}".format(u))
    
    
main()