def pali():
  import math
  n=eval(input("Enter the starting point N:\n"))
  m=eval(input("Enter the ending point M:\n"))
  n=n+1
  print("The palindromic primes are:")
  for i in range(n,m):
    p=True
    for j in range(2,(i)):
        if int(i)%j==0:
            p=False
            break
    if p==True:
      if str(i)[::-1]==str(i):
            print(i)
        
pali()        
               
            