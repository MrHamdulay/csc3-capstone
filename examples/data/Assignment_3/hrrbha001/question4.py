# calculate palindromic primes
# hs
# 16 march 2011

N = eval (input ("Enter the starting point N:\n"))
M = eval (input ("Enter the ending point M:\n"))

print ("The palindromic primes are:")

for i in range (N+1, M):
   reverse = 0
   number = i
   while number>0:
      digit = number % 10
      number = number // 10
      reverse = reverse * 10 + digit
      
   if (i == reverse):      
      prime = 1
      for j in range (2, i//2+1):
         if i % j == 0:
            prime = 0
            break
   
      if (prime == 1):
         print (i)
         
