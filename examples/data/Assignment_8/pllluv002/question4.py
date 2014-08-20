

n=eval(input("Enter the starting point N:"))
m=eval(input("Enter the ending point M:"))

def palindrome(n):
    
    str(n)
    
        
    if len(n)%2 == 0:
        if n[0] != n[-1]:
            return palindrome(n+1)
        if n[0] == n[-1]:
            return palindrome(n[1:-2])
        if n == "":
            return n+ palindrome(n+1)
        
    if len(n)%2 != 0:
        if n[0] != n[-1]:
            return palindrome(n+1)
        if n[0] == n[-1]:
            return palindrome(n[1:-2])
        if len(n) == 1:
            return n+ palindrome(n+1)   
        
print(palindrome(n))


    #def palindrome():
        
        #if n < m:
            #str(n)
            