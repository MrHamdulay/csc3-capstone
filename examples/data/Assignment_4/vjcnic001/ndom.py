# Question 2

# Mathematical functions map naturally to program functions and modules often are used to group such functions for reuse.

# In the Ndom* language, numbers use only the digits 0-5, such that instead of "tens" and "hundreds", the second and third digits represents multiples of 6 and 36 respectively. Write a Python module with the following functions for simple Ndom arithmetic, assuming that all values have at most 3 digits.
# (Reference: http://en.wikipedia.org/wiki/Senary)

# ndom_to_decimal (a), that converts a Ndom number to decimal
# decimal_to_ndom (a), that converts a decimal number to Ndom
# ndom_add (a, b), that adds 2 Ndom numbers
# ndom_multiply (a, b), that multiples 2 Ndom numbers
# Sample I/O:

# Choose test:
# d 12
# calling function
# called function
# 20
# Sample I/O:

# Choose test:
# n 20
# calling function
# called function
# 12
# Sample I/O:

# Choose test:
# a 123 141
# calling function
# called function
# 304
# Sample I/O:

# Choose test:
# m 13 14
# calling function
# called function
# 230
# Save your module as ndom.py. The main program has been supplied as question2.py - use this to test your program and do not change this file.


def ndom_add (a, b):
	x = a+b
	return x

def ndom_multiply (num1, num2):
	y = num1*num2
	return y

def decimal_to_ndom (a):
    if a == 0:
        return 0
    answer = ""
    while a > 0:
        answer = str(a%6) + answer
        a = a/6
    return int(answer)

def ndom_to_decimal (a):
    if a == 0:
        return 0
    a = str(a)
    answer = int(a[0])
    for i in a[1:]:
        answer = answer * 6
        answer = answer + int(i)
    return answer

