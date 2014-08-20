def palPrimes():
    num1 = eval(input("Enter the starting point N:\n"))
    num2 = eval(input("Enter the ending point M:\n"))
    print("The palindromic primes are:")
    for i in range(num1+1,num2):
        boole = prime(i)
        if boole == 1:
            #test if palindrome
            strInt = str(i)  
            if strInt==strInt[::-1]:
                print(i)
    
def prime(num):   
    boole = 1
    if num < 2:
        boole = 0
        
    if num == 2: 
        boole = 1 
    
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            boole = 0
           
    return boole        
       
if __name__=='__main__':
    palPrimes()
