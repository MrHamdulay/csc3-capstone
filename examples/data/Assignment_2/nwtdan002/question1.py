print("Enter a year:")
a=int(input())
if a % 400 == 0:
    print(a,"is a leap year.")
elif a % 4 == 0 and a % 100 != 0:
    print(a,"is a leap year.")
else:
    print(a,"is not a leap year.")