#Assignment 3 - Question 4
#Jayan Smart
#23 March 2014

def reverse(num): #check if number is a palendrome.
  Rnum = int(str(num)[::-1])

def prime(num):
    prime = True
    for j in range(2, round(num**0.5)+1):
        if num%j==0 and num!=j:
            prime = False
    if prime:
        print (num)
        
def PalinPrime():
    #Set start and end points (N and M respectivly)
    N = eval(input('Enter the starting point N:\n'))
    M = eval(input('Enter the ending point M:\n'))
    Rnum = ""
    j = 2
    print("The palindromic primes are:")
    
    for i in range(N+1, M):
        if i>=2:
            Rnum = int(str(i)[::-1])
            if Rnum == i:
              prime(i)
PalinPrime()
