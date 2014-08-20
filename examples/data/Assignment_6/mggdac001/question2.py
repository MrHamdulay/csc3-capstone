
from math import sqrt
def vector():
    f='{0:1.2f}'
    vector_A=[]
    vector_a=input("Enter vector A:\n")
    vector_B=[]
    vector_b=input('Enter vector B:\n')
    for num in (vector_a.split()):
        vector_A.append(num)
    #print(vector_A[1])
    for num in (vector_b.split()):
        vector_B.append(num)
    #print(vector_B)
    anbone=((eval( vector_A[0]))+(eval( vector_B[0])))
    anbtwo=((eval( vector_A[1]))+(eval( vector_B[1])))
    anbthree=((eval( vector_A[2]))+(eval( vector_B[2])))
    
    ab=((eval( vector_A[0]))*(eval( vector_B[0])))+((eval( vector_A[1]))*(eval( vector_B[1])))+((eval( vector_A[2]))*(eval( vector_B[2])))
    A=sqrt(((eval( vector_A[0]))**2)+((eval( vector_A[1]))**2)+((eval( vector_A[2]))**2))
    B=sqrt(((eval( vector_B[0]))**2)+((eval( vector_B[1]))**2)+((eval( vector_B[2]))**2))
    #print all the values
    print('A+B = [',anbone,', ',anbtwo,', ',anbthree,']',sep='')
    print('A.B',"=",ab)
    print("|A|",'=',(f.format(A)))
    print("|B|",'=',(f.format(B)))
          
vector()