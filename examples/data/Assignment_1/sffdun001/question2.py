hour=eval(input("Enter the hours:\n"))
minute=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if 0<=hour<24 and 0<=minute<60 and 0<=seconds<60:
    print("Your time is valid.")
else:
        print("Your time is invalid.")  