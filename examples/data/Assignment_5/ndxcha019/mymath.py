'''Luke Naude
program to find permutations of n
13 April'''


def get_integer(x):
   n=input("Enter "+x+":\n")
   while not n.isdigit():
      n=input("Enter "+x+":\n")
   n=eval(n)
   return n


def calc_factorial(x):
   factorial=1
   for i in range (2, x+1):
      factorial*=i
   return factorial