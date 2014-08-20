def vectors():
    import math
    #get vectors from user 
    a=input('Enter vector A:\n')
    b=input('Enter vector B:\n')
    #create two empty lists 
    veca = []
    vecb = []
    
    #split the string in the lists, make them into integers then add them to the list 
    for num in a.split():
        num = int(num)
        veca.append(num)
        
    #split the string in the lists, make them into integers then add them to the list 
    for num in b.split():
        num = int(num)
        vecb.append(num)
        
    #do the calsulations for addition, multiplication and the modulus
    print('A+B =',[(veca[0]+vecb[0]),(veca[1]+vecb[1]),(veca[2]+vecb[2])])
    print('A.B =',(veca[0]*vecb[0])+(veca[1]*vecb[1])+(veca[2]*vecb[2]))
    if veca==[0, 0, 0] and veca==[0, 0, 0]:
        print('|A| = 0.00')
        print('|B| = 0.00')
    else:
        print('|A| =',round(math.sqrt(veca[0]**2+veca[1]**2+veca[2]**2),2))
        print('|B| =',round(math.sqrt(vecb[0]**2+vecb[1]**2+vecb[2]**2),2))
    
vectors()