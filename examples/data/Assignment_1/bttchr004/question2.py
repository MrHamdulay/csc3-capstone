# Program to show validity of a input time
# Christopher Betteridge; BTTCHR004
# Due Date: 07/03/2014
# Assingment, question 2
x=eval(input("Enter the hours:\n"))
y=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))
if 0<=x<=23 and 0<=y<=59 and 0<=z<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")