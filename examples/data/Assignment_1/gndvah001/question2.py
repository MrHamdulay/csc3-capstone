x=input("Enter the hours:\n")
y=input("Enter the minutes:\n")
z=input("Enter the seconds:\n")
x=eval(x)
y=eval(y)
z=eval(z)
if (x<0 or x>23):
    print("Your time is invalid.")   
elif (y<0 or y>59):
    print("Your time is invalid.")
elif (z<0 or z>59):
    print("Your time is invalid.")
else:
    print("Your time is valid.")