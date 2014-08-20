# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

def get_integer(x):
   q1 = input("Enter" + " " + x + ":" + "\n")
   while not q1.isdigit():
      q1 = input("Enter" + " " + x + ":" + "\n")
   q1 = eval(q1)   
   return q1

def calc_factorial(n):
    factorial = 1
    for i in range (1, n+1):
       factorial *= i
    return factorial    

