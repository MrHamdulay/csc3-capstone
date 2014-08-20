# Question 4

start=eval(input("Enter the starting point N:\n"))
end=eval(input("Enter the ending point M:\n"))
print("The palindromic primes are: ")

if start<2:
    print (2)
for i in range (start+1,end,1):
    x=str(i)
    if x==x[::-1]:
        x=int(x)
        for j in range (2,x):
            if x%j==0:
                break
            elif j==(x-1):
                print(x)