n = eval(input("Enter a year:\n"))
if n <= 0:
        print(n, end=' ')
        print("is not a leap year.\n", end='')
elif n % 400 == 0:
        print(n, end=' ')
        print("is a leap year.\n", end='')
elif n % 100 == 0:
        print(n, end=' ')
        print("is not a leap year.\n", end='')
elif n % 4 == 0:
        print(n, end=' ')
        print("is a leap year.\n", end='')
else:
        print(n, end=' ')
        print("is not a leap year.\n", end='')
        
#Author: Lenard Carroll
#Student Number: CRRLEN001
