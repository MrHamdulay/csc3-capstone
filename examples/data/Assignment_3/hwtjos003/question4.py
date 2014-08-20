
start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")

for i in range(start + 1,end):
    num = str(i)
    reverse = num[::-1]
    if num == reverse:
        for j in range(2,i // 2 + 1):
            if i % j == 0:
                break        
        else:
            print(i)        
