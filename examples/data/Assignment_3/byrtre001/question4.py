import random
a=eval(input('Enter the starting point N:''\n'))
b=eval(input('Enter the ending point M:''\n'))
def odd(a,b):
   for i in range(a+1,b):
      string=str(i)
      reverse=string[::-1]
      if (string==reverse):
         c=int(string)
         x = True 
         for i in range(2,c):
            if c%i == 0:
               x = False
               break             
         if x:
            print(c)
         
   

      
print('The palindromic primes are:')
odd(a,b)

   
