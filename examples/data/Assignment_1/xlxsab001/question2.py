def time():
    a = eval(hours)
    b = eval(minutes)
    c = eval(seconds)

    if (0<=a<24) and (0<=b<60) and (0<=c<60):
        print("Your time is valid.")
        
    else:
        print ("Your time is invalid.")
        


hours=(input("Enter the hours:\n"))
minutes=(input("Enter the minutes:\n"))
seconds=(input("Enter the seconds:\n"))

time()