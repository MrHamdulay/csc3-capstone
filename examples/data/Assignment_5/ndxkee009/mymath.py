#Keegan Naidoo
#NDXKEE009
#16 April 2014

def get_integer(n):          #Method to be called 
   
   if (n=="n"):              # n permutations
      
      n = input ("Enter n:\n")   #Inputs n
   
      while not n.isdigit ():    #Exception handling for strings inputted,loops until a number(valid number) is entered
         n = input ("Enter n:\n")
   
      n = eval (n)           #Evaluates n
   
      return n               #Returns n
   
   if (n=="k"):              # k permuatations
      
      k=input("Enter k:\n")  # Inputs k
      
      while not k.isdigit(): #Exception handeling
         k=input("Enter k:\n")
      k=eval(k)              #Evaluates k  
      
      return k               #returns k

def calc_factorial(n):       # Method to be called
   
   nfactorial = 1            #Sets default nfactorial
   for i in range (1, n+1):  #Loops through from 1 to n
      nfactorial *= i        #Multiplies previous term nfactorial by i(count in the loop) first term is 1 by default
      
   return nfactorial        #Returns n factorial

#print ("Number of permutations:", nfactorial // nkfactorial)