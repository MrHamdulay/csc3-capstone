#Program to  calculate permutations
#Tsanwani Vhonani
#15 APRIL 2014

import mymath

def fact():
      #get number 'n' from user
      n=input("Enter n: \n")
      while not n.isdigit():
            n=input("Enter n: \n")
      n=eval(n)      
      
      #findng the factorial of n    
      n_fact=1
      for factor in range(n,1,-1):
            n_fact=n_fact*factor
      
      #get number 'k' from user
      k=input("Enter k:\n") 
      while not k.isdigit():
            k=input("Enter k:\n")
      k=eval(k)
      
      #finding the factorial of n-k    
      k_fact=1
      l=n-k
      for factor in range(l,1,-1):
            k_fact=k_fact*factor
      print("Number of permutations:",n_fact//k_fact)
    
fact()
        