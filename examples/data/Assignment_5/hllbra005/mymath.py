#Assignment 5: Question 3, Mymath
#Brandon Hall (HLLBRA005)
#17/04/2014 

def get_integer(letter):
    
   if(letter == "n"): 
      
      n = input ("Enter n:\n")
    
      while not n.isdigit ():
       
         n = input ("Enter n:\n")
         
      n = eval (n)    
      return n 
   
   else:      
      
      k = input ("Enter k:\n")
      
      while not k.isdigit (): 
         
         k = input ("Enter k:\n")
         
      k = eval (k)      
      return int(k)    
         
def calc_factorial(number):

   factorial = 1
   
   for i in range (1, number+1):
      
      factorial *= i 
    
   return factorial   