import sys
sys.setrecursionlimit (30000)
def palindrome(string):
    if len(string)<=1:
        return True
    else:
        if string[0]==string[len(string)-1]:
            return palindrome(string[1:len(string)-1])
        else:
            return False
def prime(a,b):

    if (b>a**(1/2)):
        return True
    if a%b==0:
        return False
    else:
        return prime(a,b+1)
def prime_palindrome(a,b):
    if a>b:
        return
    else:
        if palindrome(str(a)) and prime(a,2):
            print(a)
        prime_palindrome(a+1,b)
a=eval(input("Enter the starting point N:\n"))
if a==1:
    a= a+1
b=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
prime_palindrome(a,b)

            