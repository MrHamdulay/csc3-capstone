check=1
hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

if(0>hours or hours>23 or 0>minutes or minutes>59 or 0>seconds or seconds>59):
    print("Your time is invalid.")
else:
    print("Your time is valid.")

