hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n")) #"\n"
if minutes>=0 and  minutes<=59 and seconds>=0 and seconds<=59 and hours>=0 and hours<=23:
    print("Your time is valid.")
else:print("Your time is invalid.")
