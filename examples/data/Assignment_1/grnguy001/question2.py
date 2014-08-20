hrs = eval(input("Enter the hours:\n"))
Min = eval(input("Enter the minutes:\n"))
Sec = eval(input("Enter the seconds:\n"))
if 0<=Sec<=59 and 0<=Min<=59 and 0<=hrs<=23:
    print("Your time is valid.")
else:
    print("Your time is invalid.")