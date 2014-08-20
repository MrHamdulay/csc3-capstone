#Ikhlaas Pohplonker
#15 April 2014
#calculates the number of k-permutations of n items

#Gets an integer from the user
def get_integer (x):
      print("Enter ",x,":",sep="")
      n=input()
      while not n.isdigit ():
            print("Enter ",x,":",sep="")
            n=input()            
      n=eval(n)
      return n
#calculates the factorial
def calc_factorial (n):
      factorial=1
      for i in range(2,n+1):
            factorial=factorial*i
      return factorial


