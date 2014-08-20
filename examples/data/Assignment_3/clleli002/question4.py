#check if each number is prime or not
 #prime ifis not divisible by numbers in range(2;squareroot of number,2)
#convert prime number to string
#reverse number 
#check if reverse number == to orginal number
#if true then print number

#checks if number is prime or not. True=prime. False=not prime
def prime_check(i):
    i=abs(int(i))
    if i<2: #cannot be less than 2
        return False
    if i==2: #2 is a prime number
        return True
    if i%2==0: #cannot be even
        return False
    for j in range (3, int(i**0.5)+1,2): #if it can be diveded by numbers up and until squareroot then its not prime.
        if i%j==0:
            return False
    else: return True

def palin(number):
    number=str(number) #converts int to string
    reverse = ""
    for i in range(len(number),0,-1):
        reverse+= number[i-1] #i-1=last position of character of string.
    if reverse==number:
        
        print(reverse)
    
#Mother function.
def prime():
    print("The palindromic primes are:")
    for j in range(start+1,end):
        if prime_check(j):
            palin(j)

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
prime()