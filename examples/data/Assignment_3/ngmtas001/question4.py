#Question 4
#Pallindromic
#Assignment 3
#Tase Ngambi


def pallin():
    n = eval(input("Enter the starting point N:\n"))
    m = eval(input("Enter the ending point M:\n"))
    
    print("The palindromic primes are:")
    
   
    for x in range(n,m):
        boolean = 0
        number = str(x)
    
        if ((number[::1] == number[::-1]) and is_prime(x) == True and x!=n):
            print(number)
        
        
def is_prime(n):
    i = 2
    if n<2:
        return False
    while i <n:
        if n%i ==0:
            return False
        else:
            i +=1
    return True

pallin()