'''Program to do basic vector calculations in 3 dimensions: addition, dot product and normalization
Daniel M. Tamale
2014-04-22'''
 
import math

'''Input vectors to be stored as lists'''
def vectors():
    vectorA=[]
    vectorB=[]
    vectora=input('Enter vector A:\n')
    vectorb=input('Enter vector B:\n')
    vectorA=vectora.split(' ')
    vectorB=vectorb.split(' ')

    ''''Addition of vectors'''    
    sumAB = []   
    for i in range(3):
        f = eval(vectorA[i]) + eval(vectorB[i])
        sumAB.append(f)
        
    print ('A+B =',sumAB)
    
    ''''Product of vectors'''
    g = 0
    for i in range(3):
        h = eval(vectorA[i]) * eval(vectorB[i])
        g += h    
    print ('A.B =',g)
    
    '''To normalize vector'''
    x=0
    y=0
    for i in vectorA:
        a=(eval(i))**2
        x+=a
    print ('|A| = {0:.2f}'.format(math.sqrt(x)))
    
    for i in vectorB:
        b=(eval(i))**2
        y+=b
    print ('|B| = {0:.2f}'.format(math.sqrt(y)))
vectors()