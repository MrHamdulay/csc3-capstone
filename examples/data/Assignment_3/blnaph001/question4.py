
t0=eval(input("Enter the starting point N:"'\n'))
end=eval(input("Enter the ending point M:"'\n'))
def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True
print("The palindromic primes are:")
for a in range(t0+1,end):
    if isprime(a):
            b=str(a)[::-1]
            if str(a)==b:
                print(b)
            