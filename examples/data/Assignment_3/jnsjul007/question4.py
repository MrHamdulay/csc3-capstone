def palindrome():

   x = eval(input("Enter the starting point N:\n"))

   y = eval(input("Enter the ending point M:\n"))

   print("The palindromic primes are:")

   for i in range(x+1,y):

      if i > 1:

         for j in range(2,i):

            if (i % j) == 0:

               break

         else:

            

            if str(i)==str(i)[::-1]:

               print(i)

            

palindrome()