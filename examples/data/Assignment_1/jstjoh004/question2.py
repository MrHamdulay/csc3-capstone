#Hendrik Joosten
#JSTJOH004

hours = eval(input("\nEnter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))


if(hours>=0 and hours<=23):
    a = "true"
else:
    a = "false"
    
if(minutes>=0 and minutes<=59):
    b = "true"
else:
    b = "false"

if(seconds>=0 and seconds<=59):
    c = "true"
else:
    c = "false"

if(a=="true"):
    if(b=="true"):
        if(c=="true"):
            print("Your time is valid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
else:
    print("Your time is invalid.")