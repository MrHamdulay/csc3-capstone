def ndom_to_decimal(a):
    
    firstNum = 0
    secondNum = 0
    thirdNum = 0
    
    strOfA = str(a)
    if(len(str(a)) ==1):
        firstNum = a
    if(len(str(a)) ==2):
        firstNum = eval(strOfA[1:]) 
        secondNum = eval(strOfA[:1])
    if(len(str(a)) ==3):
        firstNum = eval(strOfA[2:]) 
        secondNum = eval(strOfA[1:2])
        thirdNum = eval(strOfA[:1])
    
    decimal = firstNum+secondNum*6+thirdNum*36
    return decimal

def decimal_to_ndom(a):
    firstNum = 0
    secondNum = 0
    thirdNum = 0
    strOfA = str(a)
    
    if(len(str(a)) ==1):
        
        if(a>5):
            newA = a - a%6
            howManySix = str(int(newA/6))
            strHowManySix = str(howManySix)
            
            return howManySix + str(a%6)
        if(a<5):
            return a
        
    if((len(str(a)) ==2) or (len(str(a)) ==3)):
        
        if(a>35):
            newA = a - a%36
            howManyThirtySix = str(int(newA/36))
            strHowManySix = str(howManyThirtySix)
            
            p = a%36
            
            newA = p - p%6
            howManySix = str(int(newA/6))
            strHowManySix = str(howManySix)
            
            return howManyThirtySix + howManySix + str(p%6)
            
            
        elif(a>5):
            newA = a - a%6
            howManySix = str(int(newA/6))
            strHowManySix = str(howManySix)
            
            return howManySix + str(a%6)
        elif(a<5):
            return a
        
def ndom_add(a,b):
    
    aDecimal = ndom_to_decimal(a)
    bDecimal = ndom_to_decimal(b)
    
    totalDecimal = aDecimal + bDecimal
    
    return decimal_to_ndom(totalDecimal)

def ndom_multiply(a,b):
    
    aDecimal = ndom_to_decimal(a)
    bDecimal = ndom_to_decimal(b)
    
    totalDecimal = aDecimal * bDecimal
    
    return decimal_to_ndom(totalDecimal)
    