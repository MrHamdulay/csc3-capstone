x=eval(input("Enter the hours:\n"))
y=eval(input("Enter the minutes:\n"))
z=eval(input("Enter the seconds:\n"))
if x<24 and y<60 and z<60 and x>=0 and y>=0 and z>=0:
    print("Your time is valid.")
if x>=24 or y>59 or z>59 or x<0 or y<0 or z<0:
    print("Your time is invalid.")