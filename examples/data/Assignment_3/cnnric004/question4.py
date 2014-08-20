import math

start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
prime = 0

remainder = 1
#if(prime != 1):
for i in range(start+1,end):
    prime=0
    #print(i)
    stri = str(i)
    rev = stri[::-1]
    if(stri == rev):
        k = eval(stri)
        for j in range(2,round(math.sqrt(i))+1):
            #print(i,j)
            remainder = k%j
            if(remainder ==0):
                prime = 1
                
        if(prime==0):
            print(i)

            
        
#    prime = 0