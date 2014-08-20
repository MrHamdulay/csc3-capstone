# Matthew Finlayson - FNLMAT001
# 29/03/14
# Assignment 4 - Question 2
#ndom.py

def ndom_to_decimal(num):
    """"converts numbers of base 6 into numbers of base 10 - decimal"""
    digits, tens, hundreds = 0,0,0
    num = str(num)
    while len(num) !=3: # makes sure that num is 3 digits long 
        num="0"+num
    
    hundreds = eval(num[:1]) # assigns the digit in the hundreds place
    tens = eval(num[1:2]) # assigns the digit in the tens place
    digits = eval(num[2:3]) # assigns the digit in the digits place
    #print(hundreds, tens, digits)
    
    decimal = hundreds*36+tens*6+digits
    return decimal

def decimal_to_ndom(num):
    """converts numbers of base 10 - decimal - to numbers of base 6"""
    hundreds = (num//36)*100
    tens = ((num%36)//6)*10
    digits = num%6
    #print(hundreds, tens, digits)

    ndom = hundreds + tens + digits
    return ndom

def ndom_add(num1, num2):
    num1 = ndom_to_decimal(num1)
    num2 = ndom_to_decimal(num2)
    ans = num1+num2
    ans = decimal_to_ndom(ans)
    return ans

def ndom_multiply(num1, num2):
    num1 = ndom_to_decimal(num1)
    num2 = ndom_to_decimal(num2)
    ans = num1*num2
    ans = decimal_to_ndom(ans)
    return ans    

if __name__ == "__main__":
    for i in range(200):
        print("decimal:", i, "\t|ndom:", decimal_to_ndom(i))