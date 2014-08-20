# Michaela Heale
# CSC1015F Assignement 1
# Question 2

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
secs = eval(input("Enter the seconds:\n"))

if (0<=hours<=23) and (0<=minutes<=59) and (0<=secs<=59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
    