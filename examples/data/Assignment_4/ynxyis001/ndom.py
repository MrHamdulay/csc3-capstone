#Jennifer Yuan (YNXYIS001)
#2 April 2014
#Assignment 4, ndom

def ndom_to_decimal(a): #converts numbers with base 6 to numbers with base 10
    hundreds = a//100 
    tens = (a%100)//10
    digits = (a%100)%10
    return (hundreds*36)+(tens*6)+digits

def decimal_to_ndom(a): #converts numbers with base 10 to numbers with base 6
    hundreds = a//36 
    tens = (a%36)//6
    digits = (a%36)%6
    return (hundreds*100)+(tens*10)+digits

def ndom_add(a,b): #adds two base 6 numbers 
    c = ndom_to_decimal(a)+ndom_to_decimal(b) #do not know how to add base six numbers so convert to base 10 numbers and then add
    answer = decimal_to_ndom(c) #convert base 10 answer back to base 6
    return answer

def ndom_multiply(a,b): # multiplies two base 6 numbers
    c = ndom_to_decimal(a)*ndom_to_decimal(b) #do not know how to multiply base six numbers so must first conver to base 10 numbers and multiply
    answer = decimal_to_ndom(c) #convert base 10 answer back to base 6
    return answer    
    