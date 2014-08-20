# program to check the validity of a time
# Peter Muriuki
# 25 february 2014

Hours = 23         # create a value for hours in the program
Minutes = 59       # create a value for minutes in the program
Seconds = 59       # create a value for seconds in the program

trial_hour = 0     # variable to store user's input for hours
trial_minute = 0   # variable to store user's input for minutes
trial_second = 0   # variable to store user's input for seconds

trial_hour = eval(input("Enter the hours:\n" ))
trial_minute = eval(input("Enter the minutes:\n"))
trial_second = eval(input("Enter the seconds:\n"))

if (trial_hour <= Hours and trial_hour >= 0) and (trial_minute <= Minutes and trial_minute >= 0) and (trial_second <= Seconds and trial_second >= 0):
            print ("Your time is valid.")
elif (trial_hour < 0 or trial_hour > Hours) or (trial_minute < 0 or trial_minute > Minutes) or (trial_second < 0 or trial_second > Seconds):
            print ("Your time is invalid.")  
