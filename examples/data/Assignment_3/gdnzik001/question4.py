#Zikho Godana
#26 March 2014
#Program to find palindromic primes between two integers supplied as input(start and end points excluded)
import math
N=eval(input("Enter the starting point N:\n"))
M=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for i in range(N+1,M):
    i_s=str(i)
    i_rev=i_s[::-1]
    i_num=int(i_rev)
    #print(i,i_num)
    if i==i_num:#Now check if the palindromes are prime
        count=0
        for a in range(2,i):
            if i%a==0:
                count+=1
        if count==0:
            print(i) 