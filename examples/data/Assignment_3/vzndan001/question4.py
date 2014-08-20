#i is an odd number generated.
#change i into a string
#revi will be the reverse of the number produced
#if i ==revi then the number is palindromic

#if i is palindromic check if dividing by 3,5,7,9,11 will produce a remainder.  if not then i is NOT a prime if a remainder is formed then i is a prime.

N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:")
for i in range(N+1,M):
     if (str(i)==str(i)[::-1]): #checking palindromes
        #print(i)
         
                    
          for j in range(2,int(i**0.5)+1): #of those odd palindromes we want to get prime numbers
               if i%j==0:                         #or i==2 or i==3 or i==5 or i==7 or i==11:  #we want it to take every palindrome odd number and divide it by cetain integers.  if any of those integers return no remainder then not a prime number
                    break
          else:
               print(i)