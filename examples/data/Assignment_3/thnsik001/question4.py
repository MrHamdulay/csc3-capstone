#Assignment 3
#22/03/2014
#q3
#thnsik001

start=eval(input("Enter the starting point N:\n"))
start+=1
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
forward =""
reverse=""
for i in range(start,end):
    forward=str(i)
    reverse=forward[::-1]
    if reverse==forward:
        factor=0
        for j in range(1,i+1):
            if i%j==0:
                factor+=1
        if factor==2:
            print(i)