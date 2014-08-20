#Assignment 2
#Question 1
#Onalerona Mosimege

result1 = "false"
result2 = "false"

year = eval(input("Enter a year:\n"))
if (year%4 == 0)  and (year%100 != 0):
    result1 = "true"
if year%400 == 0:
    result2 = "true"
if (result1 == "true") or (result2 == "true"):
        print(str(year), "is a leap year.")
else:
        print(str(year), "is not a leap year.")
