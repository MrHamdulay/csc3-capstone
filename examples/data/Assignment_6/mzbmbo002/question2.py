#Mbongeni Mazibuko
#MZBMBO002
#Assignment 6

vectorA= input('Enter vector A:\n')
vectorB= input('Enter vector B:\n')

def add(A,B):
    #function to do addition calculation for 3D vectors
    A= A.split(' ')
    B= B.split(' ')
    C=[]
    for i in range(3):
        C.append(eval(A[i])+eval(B[i]))
    return C

def dot_prod(A,B):
    #function to do dot product calculation for 3D vectors
    A= A.split(' ')
    B= B.split(' ')
    C=[]
    for i in range(3):
        C.append(str(eval(A[i])*eval(B[i])))
    C='+'.join(C)
    return eval(C)

def norm(A):
    #function to do normalization calculation for 3D vectors
    import math
    A= A.split(' ')
    C=[]
    for i in range(3):
        C.append(str(eval(A[i])**2))
    C='+'.join(C)
    return '{0:.2f}'.format(math.sqrt(eval(C)))

print('A+B =', add(vectorA,vectorB))
print('A.B =', dot_prod(vectorA,vectorB))
print('|A| =', norm(vectorA))
print('|B| =', norm(vectorB))