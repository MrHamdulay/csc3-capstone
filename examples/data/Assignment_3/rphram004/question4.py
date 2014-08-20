import math
def prime_number(x):
    if x in (0,1):
        return False
    if x%2==0 and x>2:
        return False
    for i in range(3, int(math.sqrt(x))+1,2):
        if x%i==0:
            return False
    return True

def palindrome(x):
    if str(x)==str(x)[::-1]:
        return True
    else:
        return False
    
y = eval(input("Enter the starting point N:\n"))
z = eval(input("Enter the ending point M:\n"))
a = list()

for i in range(y+1,z):
    if prime_number(i):
        if palindrome(i):
            a.append(i)
print("The palindromic primes are:")
print("\n".join(map(str, a)))