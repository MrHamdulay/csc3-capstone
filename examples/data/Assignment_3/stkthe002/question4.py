start = eval(input("Enter the starting point N: \n"))
end = eval(input("Enter the ending point M: \n"))

print("The palindromic primes are:") 

import math

for i in range(start+1,end):
     faktor = 0
     root = int(math.sqrt(i))+1
     for k in range(2,root): 
          if i%k == 0:
               faktor+=1
               break
          
     if faktor == 0:
          i = str(i)
          length = len(i)
          j = i[length::-1]
          if i==j:
               print(i)
              