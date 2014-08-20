# Question 4 - Assignment 8
# Oliver Harrison
# 6 May 2014

import sys
sys.setrecursionlimit (30000)


def prime(x, end2, y):
    if y < x:
        if x%y != 0:
            y += 1
            return prime(x, end2, y)
        else:
            return False
    else:
        return True


def pal_prime(start, end):
    if start <= end:
        if str(start)[:1] == str(start)[len(str(start))-1:]:
            y = 2
            if prime(start, end, y) and start != 1:
                print (start)
                start += 1
                return pal_prime(start, end)
            #return palindrome(string[1:len(string)-1])
            else:
                start += 1
                return pal_prime(start, end)
        else:
            start += 1
            return pal_prime(start, end)
                    
    
    







start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
pal_prime(start, end)
