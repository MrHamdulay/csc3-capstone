import math
start=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M: \n"))
end=m
start+=1
print("The palindromic primes are:")
for i in range(start,end,1):
    word=str(i)
    revword=word[::-1]
    if revword==word:
        if i==2:
            print(i)
        elif i%2!=0:
            for j in range(3,i,1):
                if i%j==0:break
            else:
                print(i)
            