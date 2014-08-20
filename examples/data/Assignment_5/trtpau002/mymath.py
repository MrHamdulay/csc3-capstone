# calculate number of k-permutations of n items
# Paul Truter
# 15 april 2014

def get_integer(number):
          integer=input("Enter " + number + ":\n")
          while not integer.isdigit ():
                    integer=input("Enter " + number + ":\n")
          integer=eval(integer)
          return integer

def calc_factorial(number):
          nfactorial=1
          for i in range(1,int(number)+1):
                    nfactorial*=i
          return nfactorial
    
    