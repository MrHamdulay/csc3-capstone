x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(x+1,y):
       k = True 
       for j in range(2, i):
              if i%j == 0:
                     k = False
                     break
       if k:
              z = str(i)
              if z == z[::-1]:
                     print (z)                                                                        
                                                                                                          