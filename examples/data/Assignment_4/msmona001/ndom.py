def ndom_to_decimal(num):
    strNum = str(num)
    length= len(strNum)
    BaseSum = 0
    for k in range(0,length):
        number= strNum[k:k+1]
        power= length-(k+1)
        base6= (int(number))*(6**power)
        BaseSum= BaseSum + base6
    return BaseSum

def decimal_to_ndom(num):
    length= len(str(num))
    newNum = ""
    temp= int(num)
    for k in range(0,(length+1)):
        base6= 6**(length-k)
        number= temp//base6
        diff=number*base6
        temp=temp-diff
        if (k>0) or (number !=0):
            newNum= newNum+ str(number)
    return newNum    


def ndom_add(num1, num2):
    no1= int(ndom_to_decimal(num1))
    no2 = int(ndom_to_decimal(num2))
    total= no1 + no2
    sum= decimal_to_ndom(str(total))
    return sum
    
def ndom_multiply(num1,num2):
    no1= int(ndom_to_decimal(num1))
    no2 = int(ndom_to_decimal(num2))    
    total= no1 * no2
    Multi= decimal_to_ndom(str(total)) 
    return Multi
        