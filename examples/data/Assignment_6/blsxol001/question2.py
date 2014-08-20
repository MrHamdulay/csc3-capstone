from math import sqrt
vector = []
def vectors():
    a = input("Enter vector A:\n")
    b = input("Enter vector B:\n")
    A = a.split()
    B = b.split()
    x = eval(A[0])+eval(B[0])
    vector.append(x)
    y = eval(A[1])+eval(B[1])
    vector.append(y)
    z = eval(A[2])+eval(B[2])
    vector.append(z)
    DOT = eval(A[0])*eval(B[0])+eval(A[1])*eval(B[1]) +eval(A[2])*eval(B[2])
    a_len = round(sqrt((eval(A[0]))**2+ (eval(A[1]))**2 + (eval(A[2]))**2),2)
    b_len = round(sqrt((eval(B[0]))**2+ (eval(B[1]))**2 + (eval(B[2]))**2),2)
    print("A+B =", vector)
    print("A.B =", DOT)
    if a_len != 0.0:
        print("|A| =", a_len)
    elif a_len == 0.0:
        print("|A| =", 0.00)
    if b_len != 0.0:
        print("|B| =", b_len)
    elif b_len == 0.0:
        print("|B| =",0.00)
vectors()