print("Enter a year:")
n = eval(input())
x = n%400
d = x//4
r = x%4
if r>0:
    print(n,"is not a leap year.")
elif r==0 and d==25:
    print(n,"is not a leap year.")
elif r==0:
    print(n,"is a leap year.")