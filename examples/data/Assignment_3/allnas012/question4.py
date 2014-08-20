def main():
   N = eval(input("Enter the starting point N:\n"))
   M = eval(input("Enter the ending point M:\n"))
   print("The palindromic primes are:")
   for i in range(N+1,M):
      if i > 1:
         for j in range(2,i):
            if (i % j) == 0:
               break
         else:
            
            if str(i)==str(i)[::-1]:
               print(i)
            
main()

