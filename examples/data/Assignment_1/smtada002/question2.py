print("Enter the hours:")
hours = eval(input())
print("Enter the minutes:")
minutes = eval(input())
print("Enter the seconds:")
seconds = eval(input())

if(hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59):
    print("Your time is valid.")
    
else:
    print("Your time is invalid.")