#find palindromic primes between two supplied integers
#Assignment 3 Question 4
#Brandon Pickup - PCKBRA002
#19 March 2014

import math
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(start+1,end):
    if i==2:
        print(i)
        continue
    elif i>2 and i%2!=0 and str(i)==str(i)[::-1]:
        j=2
        prime=True
        while j<(int(math.sqrt(i))+1) and prime==True:                       
            if i%j==0:
                prime=False
            j+=1
        if prime:
            print(i)
            
