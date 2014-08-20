#Tofunmi Olagoke
#OLGMOF001
#15 April 2014
#Program of calculating permutations

#function that turn inputted string value into a number and returns it
def get_integer (x):
   number =input("Enter"+" "+x+":""\n")
   while not number.isdigit ():
         number =input("Enter"+" "+x+":""\n")
   number = eval (number)
   return number

#calculating the factorial of a specific number
def calc_factorial (o):
   factorial=1
   i=o
   while i>=1:
      factorial=factorial*i
      i=i-1
   return factorial


