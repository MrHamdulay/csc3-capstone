# First creat function to check if a number is prime


def prime(number):
   if number!=2:
      for i in range(2,number):
       
         if number%i == 0 :
            z = "Not Prime"
            break
         else: z = "Prime"
   else: z="Prime"
      
   return z   

#Now do the rest

start= eval(input("Enter the starting point N: \n"))

end = eval(input("Enter the ending point M:  \n"))

print('The palindromic primes are:')

for i in range(start +1 , end):
   y=str(i)
   if y ==  y[ : :-1]:
      if prime(i) =="Prime":
               print(i)
      
      
      
   
        
        
        
   
        
    
    