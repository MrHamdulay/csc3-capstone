x=eval(input("Enter the hours:\n"))
y=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))
if x<=23 and x>=0 and y<=59 and y>=0 and z<=59 and z>=0:
    print("Your time is valid.")
else:
    print("Your time is invalid.")