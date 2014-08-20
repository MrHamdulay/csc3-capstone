def decimal_to_ndom(n):
    if (n//216) != 0:
        NumStr = str(n//216)
        Num = n % 216
        NumStr = NumStr + str(Num//36)
        Num = n % 36
        NumStr = NumStr + str(Num//6)        
        Num = n % 6
        NumStr = NumStr + str(Num//1)        
        
        return int(NumStr)
    elif (n//36) != 0:
        NumStr = str(n//36)
        Num = n % 36
        NumStr = NumStr + str(Num//6)        
        Num = n % 6
        NumStr = NumStr + str(Num//1)        
        
        return int(NumStr)
    elif (n//6) != 0:
        NumStr = str(n//6)        
        Num = n % 6
        NumStr = NumStr + str(Num//1)        
         
        return int(NumStr)
def ndom_to_decimal(n):
    if n//1000 != 0:
        Ndom = n//1000 * 216 # getting the 1000 part
        NumNew = n - (n//1000) * 1000 # removing the 1000 part
        
        Ndom = Ndom + (NumNew //100 * 36) # adding the 100 part
        NumNew = NumNew - ((NumNew//100) * 100) # removing the 100 part
        
        Ndom = Ndom + (NumNew //10 * 6) # adding the 100 part
        NumNew = NumNew - ((NumNew//10) * 10)
        
        Ndom = Ndom + (NumNew //1 * 1) # adding the 100 part
        NumNew = NumNew - ((NumNew//1) * 1)        
        return Ndom
    elif n//100 != 0:
        Ndom = n//100 * 36 #getting the 100 part
        NumNew = n - (n//100) * 100
        
        Ndom = Ndom + (NumNew //10 * 6) # adding the 100 part
        NumNew = NumNew - ((NumNew//10) * 10)
        Ndom = Ndom + (NumNew //1 * 1) # adding the 100 part
        NumNew = NumNew - ((NumNew//1) * 1)        
        return Ndom
    elif n//10 != 0:
        Ndom = n//10 * 6 
        NumNew = n - (n//10) * 10 
        NumNew = NumNew - ((NumNew//10) * 10) 
        Ndom = Ndom + (NumNew //1 * 1) # adding the 100 part
        NumNew = NumNew - ((NumNew//1) * 1)         
        return Ndom
        
def ndom_add(n1, n2):
    Num1 = ndom_to_decimal(n1)
    Num2 = ndom_to_decimal(n2)
    Sum_Ndom = decimal_to_ndom(Num1 + Num2)
    return Sum_Ndom


def ndom_multiply(n1, n2):
    Num1 = ndom_to_decimal(n1)
    Num2 = ndom_to_decimal(n2) 
    Multiplication = Num1 * Num2
    Multi_Ndom = decimal_to_ndom(Multiplication)
    return Multi_Ndom
