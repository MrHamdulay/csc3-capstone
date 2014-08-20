#mymath program to calculate permutations
#Robin Hall
#17/04/2014

def calc_factorial(n):
      factorial=1
      for i in range(1,n+1): #calculates factorial for number n
            factorial*=i
      return factorial

def get_integer(a):
      x=input("Enter {}:\n".format(a))
      while not x.isdigit():
            x=input("Enter {}:\n".format(a))
      x=eval(x)
      print(2+x)
