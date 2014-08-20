# Chantel Foot
# Assignment 5: mymath.py for question 3

def get_integer(x):
     if x == "n": #n is a string
          n = input("Enter n:\n")
          while not n.isdigit ():
               n = input("Enter n:\n")
          return eval(n)
    
     else:
          k = input("Enter k:\n")
          while not k.isdigit():
               k = input("Enter k:\n")
          return eval(k)
            
    
def calc_factorial(a):
     factorial = 1
     for i in range(1,a+1):
          factorial *= i
     return factorial 





        