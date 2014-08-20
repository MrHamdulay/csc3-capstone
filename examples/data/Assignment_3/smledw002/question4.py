__author__ = 'User1'
def pal(st):
    st = str(st)
    if st == st[::-1]:
        return True
    else:
        return False

def prime(x):
    div = 2
    while div < x:
        if x % div == 0 and x != 2:
            return False
        div += 1
    return True

b = eval(input("Enter the starting point N:\n"))

e = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:\n",end ="")
while b < e-1:
    b+=1
    if prime(b) == True and pal(b) == True:
        print(b)