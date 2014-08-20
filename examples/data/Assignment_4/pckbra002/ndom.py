#module for base Conversions between senary and decimal
#Assignment 4 Question 2
#2014/03/29
def ndom_to_decimal(a):#converts a base 6 number to a base 10 number
    total=0
    a = str(a)
    a = a[::-1]#reversing the string version of the number
    for i in range(len(a)):#runs for the length of the string number
        total+=int(a[i])*(6**i)#converts to decimal by multiplying each character by 6 to the power of its column number (think about units, tens, hundreds etc, this case is units, 6s and 36s)  
    return total
def decimal_to_ndom(a):#from base 10 to base 6
    final=""
    while a>0:
        final+=str(a%6)#divide the original number by its base, set the original number to its old self integer divided by the base, and add the remainder to the total
        a = a//6
    return int(final[::-1])#reverses the string so that its in appropriate format of units, 6s, 36s rather than being backwards
def ndom_add(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    sum = a+b
    return decimal_to_ndom(sum)
def ndom_multiply(a,b):
    a = ndom_to_decimal(a)
    b = ndom_to_decimal(b)
    product = a*b
    return decimal_to_ndom(product)