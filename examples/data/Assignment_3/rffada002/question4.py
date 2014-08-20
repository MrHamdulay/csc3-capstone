start = eval(input("Enter the starting point N:\n"))
end = eval(input("Enter the ending point M:\n"))
print("The palindromic primes are:")
for num in range(start+1, end):
    if all(num % i !=0 for i in range(2,num)):
        if str(num) == str(num)[::-1]:
            print(num)