print("Enter the hours:")
hours = eval(input())
print("Enter the minutes:")
minutes = eval(input())
print("Enter the seconds:")
seconds = eval(input())

if (hours<0 or hours>23):
    print("Your time is invalid.")
elif (0>hours or hours>23):
    print("Your time is invalid.")
elif (0>minutes or minutes>60):
    print("Your time is invalid.")
elif (0>seconds or seconds>60):
    print("Your time is invalid.")  
else:
    print("Your time is valid.")
    
   
