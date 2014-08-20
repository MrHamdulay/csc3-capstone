import math
def prime_number(a):
    if a in (0,1):
        return False
    if a%2==0 and a>2:
        return False
    for i in range(3, int(math.sqrt(a))+1,2):
        if a%i==0:
            return False
    return True

def palindrome(a):
    if str(a)==str(a)[::-1]:
        return True
    else:
        return False
    
b = eval(input("Enter the starting point N:\n"))
c = eval(input("Enter the ending point M:\n"))
q = list()

for i in range(b+1,c):
    if prime_number(i):
        if palindrome(i):
            q.append(i)
print("The palindromic primes are:")
print("\n".join(map(str, q)))