# the program to check the validity of time
h =input("Enter the hours:\n")
m =input("Enter the minutes:\n")
s =input("Enter the seconds:\n")
h = eval(h)
m = eval(m)
s = eval(s)
if 0<=h<=23 and 0<=m<=59 and 0<=s<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")
