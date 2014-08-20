#Tato Moaki MKXTAT001
#Python Module containing three functions to create hollow boxes of stars
#question2 Assignment4

def ndom_to_decimal(a):
    #converts a Ndom value to a decimal equivalent
    import math
    j = len(str(a)) -1
    total = 0
    myList  = [int(i) for i in str(a)] #Create a list to fill with 'a' characters
    for i in range(len(str(a))):
        total += (myList[i]*math.pow(6,j))
        j -= 1
    total = round(total)
    return(total)

def decimal_to_ndom(a):
    #converts a decimal number to Ndom
    emptyStr = ""
    base = 6
    while(a != 0):
        remainder = a % base
        a = a // base 
        emptyStr += str(remainder) #Store the remainder through each iteration
    ndomValue = int(emptyStr[::-1])#Reverse the empty string to an int value   
    return ndomValue
    
def ndom_add(a,b):
    #adds two Ndom numbers
    c = ndom_to_decimal(a) + ndom_to_decimal(b)
    return decimal_to_ndom(c)

def ndom_multiply(a,b):
    #multiply two Ndom numbers
    c = ndom_to_decimal(a) * ndom_to_decimal(b)
    return decimal_to_ndom(c)
