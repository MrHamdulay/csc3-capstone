"""finds all the palindromic primes between inputed two integers
Tafadzwa Moyo
4 May 2014"""

#increases the amount of recursion that Python will allow
import sys
sys.setrecursionlimit (30000)
#reverses string
def reverse(string):
    if len(string)>1:
        rvrse=reverse(string[1:])+string[0]
        return rvrse
    else:
        return string
#checks if a number is a prime number
p=[]
def check_prime(n, m):
    global p
    if n>2 and m>2:
            if n%(m-1)==0 or check_prime(n, m-1)==False:
                return False
            else: 
                return True
    if n==1:
        return False
    else: 
        return True
#function that finds palindromic primes
def p_prime(strt, end):
    if str(strt)==reverse(str(strt)) and check_prime(strt, strt):
        print(strt)
    if strt<end:
        p_prime(strt+1, end)

strt=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
p_prime(strt, end)