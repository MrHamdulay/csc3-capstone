#A program to calculate the number of k-permutations of n items
#Created by:Jenna Lake
#Date:15/4/2014

def get_integer(t):  #function to get integers for n and k
   if t=="n": #evaluates whether user wants to use get integer for k or n
      n = input ("Enter n:\n")
      while not n.isdigit (): #checks entered character is a digit/number else requests a new one
         n = input ("Enter n:\n")
      n = eval(n)
      return n #returns the value such that it may be used by question3.py
   elif t=="k":
      k = input ("Enter k:\n")
      while not k.isdigit ():
         k = input ("Enter k:\n")
      k = eval (k) 
      return k

def calc_factorial (s): #function that calculates the number of k factorials (of s)
      nfactorial = 1
      for i in range (1, s+1):
         nfactorial *= i
      return nfactorial
   
 