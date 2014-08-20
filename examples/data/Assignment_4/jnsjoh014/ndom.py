#JNSJOH014
#Assignment 4 Question 2

#Convert senary numbers to decimal numbers
def ndom_to_decimal (a):
    a = str(a)
    if len(a) == 1:
        num = eval(a)
        return num
    elif len(a) == 2:
        return int(a[0])*6+int(a[1])
    else:  return int(a[0])*36+int(a[1])*6+int(a[2])

#Convert decimal numbers to senary numbers
def decimal_to_ndom (a):
    a = str(a)
    nextInt = int(a)
    res = ""
    while nextInt != 0:
        res = str(nextInt%6) + res
        nextInt //= 6
    return int(res)

#Add Ndom numbers
def ndom_add (a, b):
    decA = ndom_to_decimal(a)
    decB = ndom_to_decimal(b)
    res = decimal_to_ndom(decA+decB)
    return res

#Multiply Ndom numbers
def ndom_multiply (a, b):
    decA = ndom_to_decimal(a)
    decB = ndom_to_decimal(b)
    res = decimal_to_ndom(decA*decB)
    return res