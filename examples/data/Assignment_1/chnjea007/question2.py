try:
    validity = "invalid."
    hours = eval(input("Enter the hours:\n"))
    minutes = eval(input("Enter the minutes:\n"))
    seconds = eval(input("Enter the seconds:\n"))
    
    if  0 <= hours <=23 and 0 <= minutes <=59 and 0 <= seconds <= 59:
        validity = "valid."

    print("Your time is", validity)

except NameError:
    print("Your time is invalid.")