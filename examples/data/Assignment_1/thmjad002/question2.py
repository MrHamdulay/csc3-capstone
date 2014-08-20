#Program to check if entered time is valid

print("Enter the hours:")
hours = eval(input())
print("Enter the minutes:")
minutes = eval(input())
print("Enter the seconds:")
seconds = eval(input())

if 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")