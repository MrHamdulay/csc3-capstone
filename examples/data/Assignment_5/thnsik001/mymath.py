"""Question3 Assignment5
Skhulile Thenjwayo
16 April 2014"""

def get_integer(var):
   n=""
   while not n.isdigit():
      print("Enter",var,end="")
      n = input(":\n")
   return eval(n)
   
def calc_factorial(number):
   factorial=1
   for i in range(1,number+1):
      factorial*=i
   return factorial
      
      
