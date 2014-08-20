"""program to find palindromic primes
nasonkwe hampwaye
2014-05-09"""
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
Mf=M+1 
def prime(f,s):
  #base case
  if f==0:
    return False
  if f==1:
    return False
  #recursive step
  elif b>=2 and b<math.sqrt(f):
        if f%s==0:
            return False
        else:
            return prime(f,s+1)
  else:
      return True 
    
    
def palindrome(N):
    palind=True
    #base case
    if len(range(N,Mf))<=1:
        palind=True
    else:
    #recursive step
        if N==Mf:
            return palindrome(N+1)
        else:
            palind=False
        if palind:
            print(palindrome(N))       
palindrome(N)        
        
    