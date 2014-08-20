'''To do vector calculations in 3-d
NORMAN PILUSA
April 2014'''
import math

def vector():
    #get a string vetors from user
    a=input('Enter vector A:\n')
    b=input('Enter vector B:\n')
    
    #convert strings into numbers
    a=a.split(' ')
    b=b.split(' ')
    
    # addition of vectors
    addition=[]
    for num in range(3):
        add=eval(a[num])+eval(b[num])
        addition.append(add)
        
    #multiplication of vectors
    multiplication=0
    for num in range(3):
        multiply=eval(a[num])*eval(b[num])
        multiplication+=multiply
        
    #norm of vectors
    def norm(a):
        norm=0
        for num in range(3):
            ad=(eval(a[num]))**2
            norm+=ad
        norm=math.sqrt(norm)
        return norm
    
    print('A+B =',addition)
    print('A.B =',multiplication)
    print('|A| =','{0:1.2f}'.format(norm(a)))
    print('|B| =','{0:1.2f}'.format(norm(b)))
        

vector()