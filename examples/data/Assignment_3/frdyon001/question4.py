# Name: Yonela Ford
# Student Number: FRDYON001
# Programme to return prime palindromes
# Date: 25 March 2014

def palindrome():
    x=eval(input("Enter the starting point N:\n"))
    y=eval(input("Enter the ending point M:\n"))
    z=x+1
    print("The palindromic primes are:")
    
    while z<y:
        if str(z)==str(z)[::-1]:
            for i in range(2,z):
                if z%i==0:
                    break
            else:
                if z>1:
                    print(z)
        z=z+1
        
palindrome()
        
                
        