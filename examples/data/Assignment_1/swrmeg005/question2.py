print("Enter the hours:")
a=int(input())
print("Enter the minutes:")
b=int(input())
print("Enter the seconds:")
c=int(input())
if 0<=a<=23 and 0<=b<=59 and 0<=c<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")