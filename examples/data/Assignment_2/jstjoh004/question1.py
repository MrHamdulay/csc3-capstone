#leap year program

x = eval(input("Enter a year:\n"))

y = x%400
z1 = x%4
z2 = x%100

if y==0 or (z1 == 0 and z2 != 0):
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")