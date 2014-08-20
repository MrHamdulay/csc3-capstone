'''
Prashanth Sridharan
SRDPRA001
Assignment 3
Question 04
'''

n = eval(input("Enter the starting point N:\n"))
m = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

i=n+1

def is_itPrime_(p):
    for j in range(2,int(p**0.5)+1):
        if p%j==0:
            return False

    return True

while(i<m):
    opp = str(i)
    opp=opp[::-1]
    q = str(i)
    if((q==opp) and is_itPrime_(int(q)) and (int(q)!=1)):
        print(opp)
    i+=1