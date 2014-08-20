def prime(k):
    counter = 2
    while counter<k:
        if k%counter == 0:
            return False
        counter += 1
    if k > 1:
        return True
    else:
        return False
def pal(k):
    k=str(k)
    if k == k[::-1]:
        return True
    return False
begi =  eval(input("Enter the starting point N:\n"))
endi =  eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(begi,endi):
    k=2
    if (prime(i) and pal(i)) and begi/i !=1:
        print(i)

    