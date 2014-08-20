def ndom_multiply(a,b):
    no1= int(ndom_to_decimal(a))
    no2 = int(ndom_to_decimal(b))    
    total= no1 * no2
    mult= decimal_to_ndom(str(total)) 
    return mult
        
def ndom_to_decimal(a):
    strNum = str(a)
    length= len(strNum)
    BaseSum = 0
    for j in range(0,(length)):
        number= strNum[j:j+1]
        power= length-(j+1)
        base6= (int(number))*(6**power)
        BaseSum+= base6
    return BaseSum

def decimal_to_ndom(a):
    length= len(str(a))
    newNum = ""
    temp= int(a)
    for j in range(0,(length+1)):
        base6= 6**(length-j)
        number= temp//base6
        diff=number*base6
        temp=temp-diff
        if (j>0) or (number !=0):
            newNum+= str(number)
    return newNum    


def ndom_add(a, b):
    no1= int(ndom_to_decimal(a))
    no2 = int(ndom_to_decimal(b))
    total= no1 + no2
    sum= decimal_to_ndom(str(total))
    return sum
    
