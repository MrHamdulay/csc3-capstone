x=eval(input("Enter the hours:\n"))
y=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))
if(-1<x<24 and -1<y<60 and -1<z<60):
    print("Your time is valid.")
else:
    print("Your time is invalid.")