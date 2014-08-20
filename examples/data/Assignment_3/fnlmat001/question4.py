# Matthew Finlayson - FNLMAT001
# 22/03/14
# Assignment 3 - Question 4

start = int(input("Enter the starting point N: \n"))
end = int(input("Enter the ending point M: \n"))

print("The palindromic primes are:")

for i in range(start+1, end):
    for j in range (2, i):
        if (i%j == 0):
            break
    else:
        num = str(i)
        reverseNum = num[::-1]
        if (num == reverseNum):
            print(i)