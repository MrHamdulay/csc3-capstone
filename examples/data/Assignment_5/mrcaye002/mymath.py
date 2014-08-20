# calculate number of k-permutations of n items
# bhavana harrilal
# 10 april 2014

def get_integer( param ):
   quest="Enter " + param + ":\n"
   num = input (quest)
   while not num.isdigit ():
      num = input (quest)

   return int(num);

def calc_factorial( val ):
  factorial = 1
  for i in range (1, (val+1)):
    factorial *= i
    
  return factorial;
