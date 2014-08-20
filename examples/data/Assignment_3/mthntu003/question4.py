# Assignment3
# Question4 ( Finding palindrome primes)
# 21 March 2014

N = (input("Enter the starting point N:\n"))
N=eval(N)+1
N= str(N)
M = (input("Enter the ending point M:\n"))
m = eval(M)
n = eval(N)
q = m
c= (n)
print("The palindromic primes are:")
if n<3 and m>2:
       print(2)

for i in range(c,q):
       y = N[::-1]
       if N==y:
              N = int(N)
              for j in range(2,N):
                     if N%j==0:
                            break
                     elif N%j !=0 and j!= (N-1):
                            continue
                     else:
                            print(N)
                            break
                            
       else:
              pass
       N= i+1
       N = str(N)