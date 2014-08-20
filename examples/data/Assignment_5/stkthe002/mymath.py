# calculate number of k-permutations of n items
# Thea Sitek, STKTHE002
# 16.04.2014

#get integer
def get_integer(i):
      nk = (input("Enter "+ i + ": \n"))
      while not nk.isdigit ():
         nk = (input("Enter "+ i + ": \n"))
      nk = eval (nk)      
      
      return nk

#calculate factorial      
def calc_factorial (i):   
      factorial = 1
      for i in range (1, i+1):
         factorial *= i    
         
      return factorial