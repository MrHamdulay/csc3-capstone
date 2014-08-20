# Program to check validity of time as a set of three integers
# Author: Nasreen
# Date: 25/02/14

print("Enter the hours:")
x = int(input()) # Hours input by user
print("Enter the minutes:")
y = int(input()) # Minutes input by user
print("Enter the seconds:")
z = int(input()) # Seconds input by user
if (0 <= x <= 23) and (0 <= y <= 59) and (0 <= z <= 59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")