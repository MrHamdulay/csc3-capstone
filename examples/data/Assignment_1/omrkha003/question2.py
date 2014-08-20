# program to check validity of a time
# khadeejah omar
# 27 February 2014

hour = eval(input("Enter the hours:\n"))
minute = eval(input("Enter the minutes:\n"))
second = eval(input("Enter the seconds:\n"))

if (0<=hour<=23) and (0<=minute<=59) and (0<=second<=59) :
    print("Your time is valid. ")
else: print("Your time is invalid. ")
        
