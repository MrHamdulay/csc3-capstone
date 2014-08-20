# Programme that check the validity of a time entered by the user as a set of three integers
# Developed by Emmanuel Njabulo Majozi
# MJZEMM001
# 25 FEB 2014

hour_s = eval(input("Enter the hours: \n"))
minute_s = eval(input("Enter the minutes: \n"))
second_s = eval(input("Enter the seconds: \n"))


if hour_s<0 or minute_s<0 or second_s<0:
    print ("Your time is invalid.")

elif hour_s>23 or minute_s>59 or second_s>59:
    print ("Your time is invalid.")

elif hour_s>=0 and minute_s>=0 and second_s>=0:
        print ("Your time is valid.")





