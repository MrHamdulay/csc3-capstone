"""program to calculate the number of k-permutations of n items using the binomial theorem
vuyolwethu nkosi
16 April 2014"""

#Firstly, define the get_integer function
def get_integer(s):
   print("Enter ",s,":",sep="") #getting input from user
   n=input()
   #converting the input to a digit using s.digit function
   while not n.isdigit ():
      print("Enter ",s,":",sep="")
      n=input()
   n=eval(n) #convert to integer  
   return n



#Secondly, calculate the n-factorial
def calc_factorial(n): #definition of program
   nfactorial=1 #initialising
   for j in range (1, n+1): #can't include 0 because the whole product will be multiplied by zero, which is zero. n+1 accounts for range
      nfactorial*=j #nfactorial will start from 1 and then multiply by (n of previous +1) until values of loop end
   return nfactorial


