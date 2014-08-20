#Question2
#By: Dean de Haast

hours=eval(input("Enter the hours:""\n"))
minutes=eval(input("Enter the minutes:""\n"))
seconds= eval(input("Enter the seconds:""\n"))

if hours < 0 or hours >24:
    print("Your time is invalid.")
else:
    if minutes <0 or minutes > 59:
        print("Your time is invalid.")
    else:
        if seconds<0 or seconds>59:
            print("Your time is invalid.")
        else:
            print("Your time is valid.")
  