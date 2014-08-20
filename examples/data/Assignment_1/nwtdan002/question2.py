print("Enter the hours:")
c=int(input())
print("Enter the minutes:")
d=int(input())
print("Enter the seconds:")
e=int(input())
if 0<=c<=23 and 0<=d<=59 and 0<=e<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")