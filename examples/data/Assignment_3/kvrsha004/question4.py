#Q4 of Assignment 3
#KVRSHA004
#Palindromic prime number checker

x = eval(input("Enter the starting point N:\n"))
y = eval(input("Enter the ending point M:\n"))

print("The palindromic primes are:\t")

for i in range(x+1, y):
    string = str(i)
    if (string == string[::-1]) and (all(i%j != 0 for j in range(2, i))):
        print(i)