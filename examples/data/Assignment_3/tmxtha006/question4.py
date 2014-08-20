#This prigram generates palindromic primes between given points
#Name: TEMA,    1 Hebert
#Student no.: TMXTHA006
#Date: 20 March 2014

N = eval(input("Enter the starting point N:\n")) #N is a starting point
M = eval(input("Enter the ending point M:\n")) #M is the ending point

palindrome = []
print("The palindromic primes are:")
for j in range(N+1, M):
    s = str(j)
    if s==s[::-1]:
        palindrome.append(j)

if N<2: print("2")
for i in palindrome:
    a=2
    for x in range(i):
        b = i%a
        if b!=0 and a==(i-1):
            print(i)
        elif b==0:
            continue
        a+=1  




