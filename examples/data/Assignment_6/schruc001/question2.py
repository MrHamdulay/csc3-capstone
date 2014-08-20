'''vector calculator
Ruchaan Schmidt
April 2014'''

def vectors():
    
    import math
    
    a = input ('Enter vector A:\n')         #input values of vector A
    a = a.replace (' ',',')                 #get rid of string space
    alis=a.split (',')                      #turn string into array
    
    for i in alis:
        i=int(i)
    b = input ('Enter vector B:\n')         #input values of vector B
    b = b.replace (' ',',')                 #get rid of string space
    blis=b.split (',')                      #turn string into array
    for j in blis:
        j=int(j)
    
    # addition
    add1 = int(alis[0]) + int(blis[0])
    add2 = int(alis[1]) + int(blis[1])
    add3 = int(alis[2]) + int(blis[2])
    print ('A+B = [', add1,',', add2,',', add3, ']')
    
    #dot Product
    dp = int(alis[0]) * int(blis[0])
    dp2 = int(alis[1]) * int(blis[1])
    dp3 = int(alis[2]) * int(blis[2])
    dptot = dp + dp2 + dp3
    print ('A.B = ',dptot)
    
    #Magnitude A
    for i in alis:
        if int(i)>=0:
            maga= math.sqrt(int(alis[0])**2 + int(alis[1])**2 + int(alis[2])**2)
    print ('|A| = ', round (maga,2))
    
    
    #Magnitude B
    magb= math.sqrt(int(blis[0])**2 + int(blis[1])**2 + int(blis[2])**2)
    print ('|B| = ', round (magb,2))

vectors()