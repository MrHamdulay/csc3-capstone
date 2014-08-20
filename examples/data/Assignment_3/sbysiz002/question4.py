n=eval(input("Enter the starting point N:\n"))
m=eval(input("Enter the ending point M:\n"))
result= []
for number in range(n,m):
    if str(number)==(str(number))[-1::-1]:
        factors=0
        for i in range(2,101):
            if number%i==0:
                factors+=1
        if factors<1 :
            result.append(number)
print("The palindromic primes are:")
for j in result :
    print(j)
    
               