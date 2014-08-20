#Pallindrome
#Sofia Palmer
#24/3/14

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for n in range(start+1,end-1):
    x = 2
    for x in range(2,n):
        if n % x == 0:
            break;
    if (x >= n-1):
        n = str(n)
        reverse=n[::-1]
        if n == reverse:
            print(n)