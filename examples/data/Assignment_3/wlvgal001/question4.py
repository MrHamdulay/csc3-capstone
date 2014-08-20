#palindromic 
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
i=N
    
#making sure it is only prime numbers:
for i in range(N+1,M):

#prime = True
 #        for j in range (2,i):
  #                if(i%j==0):
   #                        prime = False
    #              if prime:
                           
    if all(i%n!=0 for n in range(2,i)):
#now checking if palindromic
               s=str(i)
               s_rev= s[::-1]
               if s==s_rev:
                   print(s)


