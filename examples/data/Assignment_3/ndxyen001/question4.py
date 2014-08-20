# Yentl Naidu (NDXYEN001)
# Assignment 3
# 27 March 2014
# Question 4


n=int(input("Enter the starting point N:\n"))
m=int(input("Enter the ending point M:\n"))
print("The palindromic primes are:")  

for i in range(n+1,m):
    p=i
    k=0
    for j in range(2,p-1):
        if(p%j==0):
            k=k+1
    if(k==0):
        p=str(p)
        
        def palindrome(p):
            index=0
            check=True
            
            while index<len(p):
                if p[index]==p[-1-index]:
                    index+=1
                    return True
                return False
              
        if palindrome(p)==True:
            print(p)
                   
palindrome(p)
        
