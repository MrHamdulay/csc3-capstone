hours = eval(input("Enter the hours: \n" ))
mins = eval(input("Enter the minutes: \n"))
secs = eval(input(("Enter the seconds: \n")))
if hours>23 or hours<0 or mins>59 or mins<0 or secs<0 or secs>59: 
    print("Your time is invalid.")
else:
    print("Your time is valid.")