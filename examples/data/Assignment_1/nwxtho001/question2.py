# program to check the validity of a time entered by the user
# by: Tom New

# defines function to check validity of user inputted time
def time_check(hours, minutes, seconds):
    if hours < 0 or hours > 23:
        print("Your time is invalid.")
    elif minutes < 0 or minutes > 59:
        print("Your time is invalid.")
    elif seconds < 0 or seconds > 59:
        print("Your time is invalid.")
    else:
        print("Your time is valid.")

# asks user to input their time in hours, minutes, and seconds
hours = eval( input ("Enter the hours:\n") )
minutes = eval( input ("Enter the minutes:\n") )
seconds = eval( input ("Enter the seconds:\n") )

# calls time_check to verify user inputted time
time_check(hours, minutes, seconds)