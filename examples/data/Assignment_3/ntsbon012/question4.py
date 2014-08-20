def main():
         N=eval(input("Enter the starting point N:\n"))
         M=eval(input("Enter the ending point M:\n")) 
         print("The palindromic primes are:")
         for i in range(N+1,M):
                  palindrome(i)
def prime(Z):
         j=1
         for i in range(2,Z):
                  j=i
                  if Z%i==0:
                           break
         if j==Z-1:
                  print(Z)
def palindrome(Z):
         x=""
         y=Z
         while y!=0:
                  x = x + str(y%10)
                  y = y//10
         x = int(x)
         if Z==x:
                  prime(Z)
main()
