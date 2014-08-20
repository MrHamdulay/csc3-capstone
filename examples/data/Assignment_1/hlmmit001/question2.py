hours=eval(input("Enter the hours: \n"))
minutes=eval(input("Enter the minutes: \n"))
seconds=eval(input("Enter the seconds: \n"))
if(0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59 and type(hours)==int and type(minutes)==int and type(seconds)==int):
    print("Your time is valid.")
else:
    print("Your time is invalid.")













