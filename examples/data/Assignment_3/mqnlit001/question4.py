#palindromic primes
#26 March 2014

def palindrome():
                print("Enter the starting point N:")
                N=eval(input())
                print("Enter the ending point M:")
                M=eval(input())
                print("The palindromic primes are:")
                for i in range (N+1,M):
                                for j in range (2,i):
                                                if i%j==0: break
                                else:
                                                if(str(i)==str(i)[::-1]):
                                                                print(i)
palindrome()
        
   
  
        
