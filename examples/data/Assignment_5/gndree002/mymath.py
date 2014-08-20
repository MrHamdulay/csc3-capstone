"""Reece Gounden
Assignment 5 Q3
"""

def get_integer(q):
  if q =="n":
    n = input ("Enter n:\n")
    while not n.isdigit ():
      n = input ("Enter n:\n")
    n = eval (n)
    return n
  elif q=="k":
    k = input ("Enter k:\n")
    while not k.isdigit ():
      k = input ("Enter k:\n")
    k = eval (k)
    return k
  
def calc_factorial(w):
  f = 1
  for i in range (1, w+1):
    f *= i
  return f