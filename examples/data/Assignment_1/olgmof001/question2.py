# a program to check the validity of a time entered by the user as a set of three integers.
# Tofunmi Olagoke
# 28 February 2014
# OLGMOF001
x=eval(input("Enter the hours:\n"))
y=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))

if 0<=x<=23 and 0<=y<=59 and 0<=z<=59: #if this is true
    print("Your time is valid.")
else:
    print("Your time is invalid.")