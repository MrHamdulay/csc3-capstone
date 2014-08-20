#nasha meoli
#mlxnas004
#leap year
x = eval(input("Enter a year:\n"))
condition_1 = x%400
condition_2 = x%4
condition_3 = x%100
if (condition_1 == 0) or ((condition_2 == 0) and (condition_3 >= 1)):
    print(x,"is a leap year.")
else:
    print(x,"is not a leap year.")