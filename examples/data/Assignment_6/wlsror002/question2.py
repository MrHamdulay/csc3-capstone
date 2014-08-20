import math
Ainput= input('Enter vector A:\n')
Binput= input('Enter vector B:\n')

def vector(Ainput, Binput):
    a = Ainput.split()
    b = Binput.split()
    A=[]
    B=[]
    
    
    for i in a:
        x=int(i)
        A.append(x)
    
    for i in b:
        x=int(i)
        B.append(x) 
        
    AB=(A[0]*B[0])+(A[1]*B[1])+(A[2]*B[2])
    normA= math.sqrt(A[0]**2+A[1]**2+A[2]**2)
    normB= math.sqrt(B[0]**2+B[1]**2+B[2]**2)
    
    print('A+B = [',(A[0]+B[0]),', ',(A[1]+B[1]),', ',(A[2]+B[2]),']', sep='')
    print('A.B =', AB)
    print('|A| =', round(normA,2))
    print('|B| =', round(normB,2))
        
    
    
vector(Ainput, Binput)
    