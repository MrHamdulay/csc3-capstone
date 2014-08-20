def ndom_to_decimal(a):
    num = len(str(a))
    if num == 1:
        return(a)
    if num == 2:
        answer1 = int(a)
        newnum1 = str(answer1)
        finalans = int(newnum1[0:1])*6 + int(newnum1[1:2])
        return (finalans)
    if num == 3:
        answer2 = int(a)
        newnum2 = str(answer2)
        finalans2 = int(newnum2[0:1])*36 + int(newnum2[1:2])*6 + int(newnum2[2:3])
        return (finalans2)
        
def decimal_to_ndom (a):
    if len(str(a)) ==1:
        if a <=6:
            return a
        else: return a+4     
    
    elif len(str(a)) ==2:
        num1 = a//6
        remainder1 = a%6
        num2 = num1//6
        remainder2 = num1%6
        num3 = num2//6
        remainder3 = num2%6        
        new_decNumStr = str(remainder3)+str(remainder2)+str(remainder1)
        new_decNum = int(new_decNumStr)
        return(new_decNum)

    elif len(str(a)) ==3:
        num1 = a//6
        remainder1 = a%6
        num2 = num1//6
        remainder2 = num1%6
        num3 = num2//6
        remainder3 = num2%6
        num4 = num3//6
        remainder4 = num3%6         
        new_decNumStr = str(remainder4)+str(remainder3)+str(remainder2)+str(remainder1)
        new_decNum = int(new_decNumStr)
        return(new_decNum)
    

def ndom_add(a,b):
    x=   ndom_to_decimal(a)
    y = ndom_to_decimal(b)    
    z=x+y
    w=decimal_to_ndom(z)
    return w
    

def ndom_multiply(a,b):
    x=   ndom_to_decimal(a)
    y = ndom_to_decimal(b)
    zz=(x*y)
    w=decimal_to_ndom(zz)
    return w   