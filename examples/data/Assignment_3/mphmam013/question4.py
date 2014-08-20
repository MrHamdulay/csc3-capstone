# question 4
# assignment 3
# mphuthi mamorena
def isprime(v):
     v*=1.0
     for divisor in range(2,int(v**0.5)+1):
          if v/divisor==int(v/divisor):
               return False
     return True

def main():
     n=eval(input("Enter the starting point N: \n"))
     m=eval(input("Enter the ending point M: \n"))
     print("The palindromic primes are: ")
     for i in range(n+1,m):
          i=str(i)
          j=i[::-1]
          if i==j:
               x=isprime(int(i))
               if x==True:
                    print(i)              
        
main()
            