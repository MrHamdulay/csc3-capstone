"""Program to do basic vector calculations
Shane Robinson
19 April 2014"""

print("Enter vector A:")
A = input()
print("Enter vector B:")
B = input()
vector_A = A.split()    #create list from input
vector_B = B.split()    #create list from input

def add():
    x = eval(vector_A[0])+eval(vector_B[0])
    y = eval(vector_A[1])+eval(vector_B[1])
    z = eval(vector_A[2])+eval(vector_B[2])
    print("A+B =", [x, y, z])

add()

def dot():
    x = eval(vector_A[0])*eval(vector_B[0])
    y = eval(vector_A[1])*eval(vector_B[1])
    z = eval(vector_A[2])*eval(vector_B[2])
    print("A.B =", x+y+z)

dot()

def magnitude():
    magA = (eval(vector_A[0])**2+eval(vector_A[1])**2+eval(vector_A[2])**2)**(0.5)
    magB = (eval(vector_B[0])**2+eval(vector_B[1])**2+eval(vector_B[2])**2)**(0.5)
    print("|A| =", "{:0.2f}".format(magA))
    print("|B| =", "{:0.2f}".format(magB))

magnitude()