# a program that Finds all palindromic primes between two integers supplied as input (start and end points are excluded)
# mashau zwivhuya
# 20 march 2014
def main():
   start=input("Enter the starting point N:\n")
   endd=input("Enter the ending point M:\n")
   startt=eval(start)
   enddd=eval(endd)
   print("The palindromic primes are:")
   for i in range(startt+1,enddd):
      if str(i)==str(i)[::-1]:
         num = True
         for j in range(2,i):
            if i%j==0:
               num=False
         if num==True:
            print(i)
         
main()            
