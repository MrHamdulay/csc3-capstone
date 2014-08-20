x=eval(input('Enter the starting point N:\n'))
y=eval(input('Enter the ending point M:\n'))

print('The palindromic primes are:')
for n in range(x+1,y):
    def conv(n):
        t=str(n) # converts prime to string
        if t[:]==t[::-1]:# reverses the string prime number
            print(n) #prints the palindrome
        
    def isprime(n):
        if n<2:
            return False
        elif n==2:
            pass
        
        elif not n & 1:
            return False
        for x in range(3, int(n**0.5)+1,2):
            if n%x==0:
                return False
        conv(n)
    isprime(n)