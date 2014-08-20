import math
def vectors():
    print('Enter vector A:')
    A1 = input()
    A1 = A1.split(" ")
    print('Enter vector B:')
    B1 = input()
    B1 = B1.split(" ")
    
    AB1 = eval(A1[0])+eval(B1[0])
    AB2 = eval(A1[1])+eval(B1[1])
    AB3 = eval(A1[2])+eval(B1[2])
    print('A+B = ','[',AB1,', ',AB2,', ',AB3,']',sep='')
    
    A_B1 = eval(A1[0])*eval(B1[0])
    A_B2 = eval(A1[1])*eval(B1[1])
    A_B3 = eval(A1[2])*eval(B1[2])
    AB = A_B1 + A_B2 + A_B3 
    print('A.B =',AB)
    
    A = math.sqrt(eval(A1[0])**2 + eval(A1[1])**2 + eval(A1[2])**2)
    if A == 0.0:
        print('|A| = 0.00')
    else:
        print('|A| =',round(A,2))
    
    B = math.sqrt(eval(B1[0])**2 + eval(B1[1])**2 + eval(B1[2])**2)
    if B == 0.0:
            print('|B| = 0.00')    
    else:
        print('|B| =',round(B,2))
    

vectors()