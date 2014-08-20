def ndom_to_decimal(a):
    str_Num = str(a)
    length= len(str_Num)
    Base_Sum = 0
    for j in range(0,(length)):
        numb= str_Num[j:j+1]
        power= length-(j+1)
        base6= (int(numb))*(6**power)
        Base_Sum+= base6
    return Base_Sum


def decimal_to_ndom(a):
    length= len(str(a))
    new_Num = ""
    tem= int(a)
    for j in range(0,(length+1)):
        base6= 6**(length-j)
        numb= tem//base6
        diff=numb*base6
        tem=tem-diff
        if (j>0) or (numb !=0):
            new_Num+= str(numb)
    return new_Num    


def ndom_multiply(a,b):
    N1= int(ndom_to_decimal(a))
    N2 = int(ndom_to_decimal(b))    
    total= N1 * N2
    mult= decimal_to_ndom(str(total)) 
    return mult
        
def ndom_add(a, b):
    N1= int(ndom_to_decimal(a))
    N2 = int(ndom_to_decimal(b))
    total= N1 + N2
    sum= decimal_to_ndom(str(total))
    return sum

 


    
