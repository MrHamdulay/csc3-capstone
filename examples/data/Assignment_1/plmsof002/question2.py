# Program to check the validity of time
# 3/3/14
# Sofia Palmer

def main():    
    hours = input("Enter the hours: \n")
    minutes = input("Enter the minutes: \n")
    seconds = input("Enter the seconds: \n")
    hours = eval(hours)
    minutes = eval(minutes)
    seconds = eval(seconds)
    if hours < 0 or hours > 24 or minutes < 0 or minutes > 60 or seconds < 0 or seconds > 60 :
        print ("Your time is invalid.")
    else :
        print ("Your time is valid.")
main()