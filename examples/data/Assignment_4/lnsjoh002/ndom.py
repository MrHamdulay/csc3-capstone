def ndom_to_decimal(a):
    a=str(a)
    if len(a)== 1:
        return a
    elif len(a)==2:
        first= a[0]
        digit1 = eval(first)
        digit1*=6
        second= a[1]
        digit2 = eval(second)
        y = digit1 + digit2
        return y
    
    elif len(a)==3:
        first=a[0]
        digit1 = eval(first)
        digit1=36
        second=a[1]
        digit2=eval(second)
        digit2*=6
        third=a[2]
        digit3=eval(third)
        y = digit1 +digit2 + digit3
        return y
    
        
            
    

def decimal_to_ndom(a): 
    if a<=5:
        return a
        
    elif a <= 35:
        x = a%6
        tens = (a-x)//6
        ten_digit=str(tens)
        single_digit=str(x)
        y =ten_digit + single_digit
        y=eval(y)
        return y
    
    
    elif a<= 215:
        x = a%36
        hundred = (a-x)//36
        z = x%6
        ten = (x-z)//6
        single = z
        hundred_digit = str(hundred)
        ten_digit = str(ten)
        single_digit = str(single)
        y = hundred_digit +ten_digit+ single_digit
        y= eval(y)
        return y
    
    
def ndom_add (a, b):
    z =  ndom_to_decimal(a) + ndom_to_decimal(b)
    y = decimal_to_ndom(z)
    return y


def ndom_multiply (a, b):
    z = (ndom_to_decimal(a)) * (ndom_to_decimal(b))
    y = decimal_to_ndom(z)
    return y
   
    
    
    
    
if __name__ =='__main__':
    x= input("Do u want to convert to (N)dom or (D)ecimal? \n")
    y = eval(input("Enter the number: \n"))
    
    if x=='N':
        print("The Ndom number is:", decimal_to_ndom(y))
        
    elif x=='D':
        print("The decimal number is:",ndom_to_decimal(y))
             
    
        
        
        
    
    
    

    
    
        
    