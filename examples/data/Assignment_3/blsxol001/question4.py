# a program to display all palindrome numbers in any given range
# xola waseMbo
# 18/04/2014

N = input("Enter the starting point N:\n")
while not N.isdigit():
    N = input("Enter the starting point N:\n")
N = eval(N)
M = input("Enter the ending point M:\n")
M = eval(M)
N +=1
print("The palindromic primes are:")
for i in range(N,M):
    y = True    
    if(str(i) == str(i)[::-1]):
        if(i>2):
            for j in range(2,i):
                if(i%j==0):
                    y = False
                    break
            if y:
                
                print(i)
    