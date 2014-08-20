"""# calculate number of k-permutations of n items
# DIVAN JAGERS
#JGRDIV001
# 15 april 2014"""

def get_integer (x) :
   a = input ("Enter"+" "+ x +":\n")
   while not a.isdigit():
      a = input ("Enter "+ x+":\n") #RETURNS WHAT EVER VALUE THE USER ENTERS
   return eval(a)
def calc_factorial(x):
   #x= eval(x)
   y=1
   for i in range (1, x+1):    #RETURNS THE FACTORIAL VALUE FOR A GIVEN VARIABLE
      y*= i
   return y