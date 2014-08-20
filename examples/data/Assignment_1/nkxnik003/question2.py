#Question 2 - Assignment 1
#Program for error handling of time input
#Nikhil Jiten Naik (NKXNIK003)
#3rd of March 2014

userHoursText   = input("Enter the hours: \n")
userHours= eval(userHoursText)
userMinutesText = input("Enter the minutes: \n")
userMinutes= eval(userMinutesText)
userSecondsText = input("Enter the seconds: \n")
userSeconds= eval(userSecondsText)



if userHours < 0 or userHours > 23 or userMinutes < 0 or userMinutes > 59 or userSeconds < 0 or userSeconds > 59:
 print("Your time is invalid.")
 
else:
 print("Your time is valid.")
 







