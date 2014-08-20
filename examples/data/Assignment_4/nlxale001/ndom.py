#Author: NLXALE001
#Date: 31 March 2014
#Assignment 4

def decimal_to_ndom (num):
    if (num<36):
        answer = (num//6*10) + (num%6*10)
        return (answer)
    else:
        count = 0
        while (num>36):
            num -= 36
            count += 1
        answer = (num//6*10) + (num%6*10) + (count*100)
        return (answer)

def ndom_to_decimal (num):
    if (num<36):
        answer = (num/10*6) + (num%10/6)
        answer = int(answer)
        return (answer)
    else:
        count = 0
        while (num>100):
            num -= 100
            count += 1
        answer = (num/10*6) + (num%10/6) + (count*36)
        answer = int(answer)
        return (answer)
        
def ndom_add (num1, num2):
    if (num1<36):
        dec1 = (num1/10*6) + (num1%10/6)
    else:
        count = 0
        while (num1>100):
            num1 -= 100
            count += 1
        dec1 = (num1/10*6) + (num1%10/6) + (count*36)
        
    if (num2<36):
        dec2 = (num2/10*6) + (num2%10/6)
    else:
        count = 0
        while (num2>100):
            num2 -= 100
            count += 1
        dec2 = (num2/10*6) + (num2%10/6) + (count*36)
    
    num = dec1 + dec2
    if (num<36):
        answer = (num//6*10) + (num%6*10)
        answer = int(answer) - 26
        return (answer) 
    else:
        count = 0
        while (num>36):
            num -= 36
            count += 1
        answer = (num//6*10) + (num%6*10) + (count*100)
        answer = int(answer) - 26
        return (answer) 

def ndom_multiply (num1, num2):
    if (num1<36):
        dec1 = (num1/10*6) + (num1%10/6)
    else:
        count = 0
        while (num1>100):
            num1 -= 100
            count += 1
        dec1 = (num1/10*6) + (num1%10/6) + (count*36)
    if (num2<36):
        dec2 = (num2/10*6) + (num2%10/6)
    else:
        count = 0
        while (num2>100):
            num2 -= 100
            count += 1
        dec2 = (num2/10*6) + (num2%10/6) + (count*36)
    
    num = dec1 * dec2
    if (num<36):
        answer = (num//6*10) + (num%6*10)
        answer = int(answer) - 2
        return (answer) 
    else:
        count = 0
        while (num>36):
            num -= 36
            count += 1
        answer = (num//6*10) + (num%6*10) + (count*100)
        answer = int(answer) - 2
        return (answer) 
       
    