"""program to provide output for calculating the number of k-permutations of n-items --- Binomial Theorem
Thabiso Beau
15 April 2014"""

#PART 1: starting the process of the calculation
def get_integer(x):
   #tell user to enter a number, n, in order to calculate n-factorial
   print("Enter ",x,':',sep='')
   n = input()
   #convert n to a digit using s.digit
   while not n.isdigit ():
      print("Enter ",x,':',sep='')
      n= input()
   n = eval (n)   
   return n
   #NOTE TO SELF: make sure that the variables correspond----> n = get_integer ("n")
   #NOTE TO SELF: make sure that the variables correspond----> k = get_integer ("k")

#k = input ("Enter k:\n")
#while not k.isdigit ():
   #k = input ("Enter k:\n")
#k = eval (k)


#PART 2: calculating n-factorial
def calc_factorial(n):
   nfactorial = 1
   for i in range (1, n+1):
      #n! will start from and multiply incrimentally within loop
      nfactorial *= i
   return nfactorial

#nkfactorial = 1
#for i in range (1, n-k+1):
   #nkfactorial *= i

#print ("Number of permutations:", nfactorial // nkfactorial)
