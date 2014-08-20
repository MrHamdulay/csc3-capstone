#ASSIGNMENT 5
#QUESTION 3
#NLTWES001

#Function to get integers
def get_integer(letter):
   number=input("Enter "+letter+":""\n")
   while not number.isdigit():
      number=input("Enter "+letter+":""\n")
   return eval(number)

#Calculate factorial
def calc_factorial(x):
   factorial=1
   for i in range(1,x+1):
      factorial*=i
   return factorial
