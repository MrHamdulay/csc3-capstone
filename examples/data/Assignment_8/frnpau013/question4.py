"""finds all palindromic primes between two integers
Paul Freund
2014"""

import sys
sys.setrecursionlimit (30000)

def prime(n):
    """checks if a number is prime"""
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for y in range(3, int(n**0.5)+1, 2):
        if n % y == 0:
            return False
    return True


def pal_prime_count(_list, start, end):
    """compiles a list of palindromic primes between two integers, 
    with list of [] supplied"""
    if start > end:
        return _list
    else:
        if str(start)[::-1] == str(start) and prime(start) == True:
                _list.append(start)
                return pal_prime_count(_list, start + 1, end)
        else:
            return pal_prime_count(_list, start + 1, end)
        
def list_printer(_list):
    """prints a list recursively"""
    if _list == []:
        pass
    else:
        print(_list[0])
        list_printer(_list[1:])

def main():
    """formats input and output for marker"""
    start = eval(input("Enter the starting point N:\n"))
    end = eval(input("Enter the ending point M:\n"))
    primes = pal_prime_count([], start, end)
    print("The palindromic primes are:")
    list_printer(primes)
    
if __name__ == '__main__':
    main()