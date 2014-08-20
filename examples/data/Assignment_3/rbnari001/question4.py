def is_prime(num):
    for j in range (2,num):
        if (num%j) == 0:
            return False
    return True

start = eval(input ("Enter the starting point N:\n"))
end = eval(input ("Enter the ending point M:\n"))

print ("The palindromic primes are: ")
for i in range (start+1,end):
    if is_prime(i):
        i = str(i)
        x = i[::-1]
        if x == i:
            print (int(i))