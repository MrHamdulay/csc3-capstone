# Question 4 - Assignment 3
# Oliver Harrison HRROLI001
# 21 March 2014

n=eval(input("Enter the starting point N: \n"))
m=eval(input("Enter the ending point M: \n"))
print("The palindromic primes are:")
def prime(x):
    x==True
    for j in range(2,x):
        if x%j==0:
            x==False
            break
        
        
for i in range(n+1,m):
    if i==int(str(i)[::-1]):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
    else:
        continue
        
        
    