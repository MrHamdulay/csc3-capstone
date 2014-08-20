# calculate number of k-permutations of n items
# Nevarr Pillay - PLLNEV006
# 10 april 2014

def get_integer(letter):
   output = "Enter " + letter.lower() + ":\n"
   num = input (output)
   while not num.isdigit ():
      num = input (output)
   num = eval (num) 
   return num

def calc_factorial(num):
   factorial = 1
   for i in range(1,num+1):
      factorial *= i
   return factorial   

