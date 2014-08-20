hours = eval(input("\nEnter the hours: "))
minutes = eval(input("\nEnter the minutes: "))
seconds = eval(input("\nEnter the seconds: "))

if(0<=hours<=23):
    if(0<=minutes<=59):
        if(0<=seconds<=59):
            print("\nYour time is valid.")
        else:
            print("\nYour time is invalid.")
    else:
        print("\nYour time is invalid.")
else:
    print("\nYour time is invalid.")