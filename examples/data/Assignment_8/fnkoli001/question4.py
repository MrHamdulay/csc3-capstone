import sys

sys.setrecursionlimit(30000)

# From http://www.daniweb.com/software-development/python/code/216880/check-if-a-number-is-a-prime-number-python
def calc_prime(check, number):
    if check == int(number**0.5) + 1 or number == 3:
        return True
    
    if number % check == 0:
        return False
    else:
        return calc_prime(check + 1, number)


def is_prime(n):
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
        # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    return calc_prime(3, n)


def paln_primes(start, stop):
    if start == stop:
        if is_prime(start) and str(start) == string_eater(str(start)):
            print(start)
    elif is_prime(start) and str(start) == string_eater(str(start)):
        print(start)
        paln_primes(start + 1, stop)
    else:
        paln_primes(start + 1, stop)
        
        
def string_eater(s):
    if s == "":
        return ""
    else:
        return string_eater(s[1:len(s)]) + s[0]

inp_start = eval(input("Enter the starting point N:\n"))
inp_end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
paln_primes(inp_start, inp_end)