# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

n = input ("Enter n:\n")
while not n.isdigit ():
   n = input ("Enter n:\n")
n = eval (n)  

k = input ("Enter k:\n")
while not k.isdigit ():
   k = input ("Enter k:\n")
k = eval (k)


def get_integer(string1):
   string1 = string1.lower()
   if string1 == "n":
      return n
   
   elif string1 == "k":
      return k   

def calc_factorial(num):
   factorial = 1
   for i in range (1, num+1):
      factorial *= i
   return factorial
