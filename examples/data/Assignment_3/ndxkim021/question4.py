fnum = eval(input("Enter the starting point N: \n"))
snum = eval(input("Enter the ending point M: \n"))
output = print("The palindromic primes are: ")
for k in range(fnum+1,snum):
   
   y = int(str(k)[::-1]) 
   if y == k:
      prime = 't'
      i = 2
      while i<k:
         if k%i==0 & i!=k:
           
            prime = 'f'
         i +=1
           
      if prime == 't':
            print(k)   
    
    
