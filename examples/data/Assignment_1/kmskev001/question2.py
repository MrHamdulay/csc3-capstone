# program that tells you whether input time is valid or not 
# 26/02/2014
# kmskev001 kevin kumasamba

print("Enter the hours:")
hours = eval(input())
print("Enter the minutes: ")
minutes = eval(input())
print("Enter the seconds: ")
seconds = eval(input())
if hours > 23 or hours < 0 or minutes < 0 or minutes > 59 or seconds < 0 or seconds > 59:
    print("Your time is invalid.")
else:
    print("Your time is valid.")
    