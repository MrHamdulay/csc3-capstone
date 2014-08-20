# Finding a leap year
# Andrew Forson
# FRSAND012

a = eval(input("Enter a year: \n"))
if a%4 == 0 and a%100 != 0:
    print(a, "is a leap year.")
elif a%400 == 0:
    print(a, "is a leap year.")
else:
    print(a, "is not a leap year.")
