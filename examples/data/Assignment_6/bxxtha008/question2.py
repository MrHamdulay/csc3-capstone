"""program to do vector calculations - addition, subtraction & normalisation
Thabiso Beau
Assignment 6: #question2.py
23 April 2014"""

def main():
    import math
    #eerste deel - om syfers vir Vector A te kry
    vectA = input('Enter vector A:\n')
    vectA = vectA.split( ) #enkele syfers
    A =[] #oop lys sodat nommers in kan gaan
    for i in vectA:
        A.append(eval(i)) #evalueer stryk as nommer
        
       
    #tweede deel - om syfers vir Vector B te kry// doen dieselfde as wat ons vir die 1ste deel gedoen het
    vectB = input('Enter vector B:\n')
    vectB = vectB.split( )
    B = []
    for j in vectB:
        B.append(eval(j))
    
    a= A[0]+B[0]
    b= A[1]+B[1]
    c= A[2]+B[2]
    
    d = A[0]*B[0]
    e = A[1]*B[1]
    f = A[2]*B[2]
    
    g = A[0]**2
    h = A[1]**2
    k = A[2]**2
    
    m = B[0]**2
    n = B[1]**2
    p = B[2]**2
    print("A+B =",[a, b, c])
    print('A.B =',(d+e+f))
    print("|A| =", "{0:.2f}".format((math.sqrt(g+h+k))))
    print('|B| =', '{0:.2f}'.format((math.sqrt(m+n+p))))
main()