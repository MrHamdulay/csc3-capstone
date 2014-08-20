"""mymath: functions that will be used by question 3
#Rama Raphalalani
#15-04-2014"""

#Function enables us to get an integer from an input
def get_integer(x):
   n = ''
   while not n.isdigit ():
      n = input ("Enter "+x+":\n")
   return int(n)

#function to do all the maths to calculate the factorials by question 3      
def calc_factorial(x):
   
   nfactorial = 1
   for i in range (1,x + 1):
      nfactorial *= i 
   return nfactorial
   
