hour=int(input("Enter the hours:"+"\n" ))
minute=int(input("Enter the minutes:" +"\n"))
second=int(input("Enter the seconds:" +"\n"))
if (0<=hour<=23):
    if (0<=minute<=59):
        if (0<=second<=59):
            print("Your time is valid.")
        else:
            print("Your time is invalid.")
    else:
        print("Your time is invalid.")
    
else:
    print("Your time is invalid.")

