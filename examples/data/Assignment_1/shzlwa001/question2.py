print("Enter the hours:")
h=eval(input())
print("Enter the minutes:")
m=eval(input())
print("Enter the seconds:")
s=eval(input())
def RealTime():
    if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
RealTime()