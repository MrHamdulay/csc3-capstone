hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))
valid = hours >= 0 and hours < 24 and \
    minutes >= 0 and minutes < 60 and \
    seconds >= 0 and seconds < 60
print("Your time is " + ("valid" if valid else "invalid") + ".")
