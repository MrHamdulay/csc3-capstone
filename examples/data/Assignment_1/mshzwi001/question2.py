# A program to check the validity of time
# Mashau zwivhuya
# 27 February 2014
hour=input("Enter the hours:\n")
hour_eval=eval(hour)
minute=input("Enter the minutes:\n")
minute_eval=eval(minute)
seconds=input("Enter the seconds:\n")
seconds_eval=eval(seconds)
if 0<=hour_eval<=23 and 0<=minute_eval<60 and 0<=seconds_eval<60:
                   print("Your time is valid.")
else :
                   print("Your time is invalid.")