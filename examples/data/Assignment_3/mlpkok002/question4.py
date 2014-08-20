import math
def palindrome():
        for i in range((M+1),N):
                x=(str(i)[::-1])
                x=int(x)
                if x==i:
                        y=True 
                        for j in range(2,int(math.sqrt(i)+1)):
                                if (x%j==0):
                                        y=False
                                        break
                        if y==True:
                                print(x)
M=eval(input("Enter the starting point N:\n"))
N=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")                                
palindrome()
