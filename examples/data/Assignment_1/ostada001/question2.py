hours = input("Enter the hours:\n")
minutes = input("Enter the minutes:\n")
seconds = input("Enter the seconds:\n")


if hours.isdigit() and minutes.isdigit() and seconds.isdigit() :
    hours = eval(hours)
    minutes = eval(minutes)
    seconds = eval(seconds)
    if hours >=0 and hours < 24 and minutes >= 0 and minutes <= 60 and seconds >= 0 and seconds <= 60 :
        print("Your time is valid.")
    else:
            print("Your time is invalid.")
            
else:
    print("Your time is invalid.")



   
    
    
    