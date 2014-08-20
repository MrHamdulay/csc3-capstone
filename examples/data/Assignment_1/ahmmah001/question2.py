# Time validity
# Mahnoor Ahmed
# AHMMAH001

x=input("Enter the hours:\n")
x=eval(x)
y=input("Enter the minutes:\n")
y=eval(y)
z=input("Enter the seconds:\n")
z=eval(z)
if 0<=x<=23 and 0<=y<=59 and 0<=z<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")