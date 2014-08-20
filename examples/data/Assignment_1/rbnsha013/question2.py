hour = eval(input("Enter the hours: "))
minute = eval(input("\nEnter the minutes: "))
second = eval(input("\nEnter the seconds: "))
        
if (0<=hour<=23) and (0<=minute<=59) and (0<=second<=59):
    print("\nYour time is valid.")
else:
    print("\nYour time is invalid.")