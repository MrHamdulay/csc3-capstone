def ndom_to_decimal(a):
    if a >= 100:
        Hundereds = a//100
        
        Leftover = a%100
        
        Tens = Leftover//10
        
        Units = Leftover%10
        
        DecimalNumber = (Hundereds*36) + (Tens*6) + Units
    
    elif (10 <= a < 100):
        Tens = a//10
        Units = a%10
        DecimalNumber = (Tens*6) + Units
        
    else:
        Units = a%10
        DecimalNumber = Units
        
    return DecimalNumber
        


def decimal_to_ndom(a):
    if a >= 36:
        Hundereds = a//36
            
        Leftover = a%36
        
        Tens = Leftover//6
            
        Units = Leftover%6
            
        NdomNumber = (Hundereds*100) + (Tens*10) + Units
              
        
    elif (6 <= a < 36):
        Tens = a//6
        Units = a%6
        NdomNumber = (Tens*10) + Units
            
    else:
        Units = a%6
        NdomNumber = Units
            
    return NdomNumber    
    


def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    
    DecimalAddition = a + b
    
    Final = decimal_to_ndom(DecimalAddition)
    
    return Final 
    


def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)  
    
    DecimalMultiplication = a*b
    
    Final = decimal_to_ndom(DecimalMultiplication)
    
    return Final






if __name__ == "__main__":
    
    TestType = str.lower(input("Choose test:\n"))
    
    TestType = TestType.split()
    
    
    if TestType[0] == 'n':
        print("calling function\n", "called function", sep="")
        print(ndom_to_decimal(int(TestType[1])))
        
    
    if TestType[0] == 'd':
        print("calling function\n", "called function", sep="")
        print(decimal_to_ndom(int(TestType[1])))
        
    
    if TestType[0] == 'a':
        print("calling function\n", "called function", sep="")
        print(ndom_add(int(TestType[1]),int(TestType[2])))
        
    
    if TestType[0] == 'm':
        print("calling function\n", "called function", sep="")
        print(ndom_multiply(int(TestType[1]),int(TestType[2])))    
           
        