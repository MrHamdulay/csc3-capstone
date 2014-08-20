def prime(i):
    
    i = abs(int(i))
    
    if i < 2:
        return False
    
    #2 is prime
    if i == 2:
        return True
    
    #check if even
    if i%2 == 0:
        return False
        
    for divisor in range (3, int(i**0.5)+1, 2):
        
        if i%divisor == 0:#number isnt prime
            return False
        
    else:
        return True

def palin (number):
    
    backwards = ""
    
    #reverses the number
    for i in range(len(number),0,-1):
        backwards += number[i-1]
    
    #checks that the number is same reversed as it is forwards
    if (number == backwards):
        print(number)


def mofo():
    for i in range (start+1, end):
        if prime(i):
            palin(str(i))
        
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
mofo()