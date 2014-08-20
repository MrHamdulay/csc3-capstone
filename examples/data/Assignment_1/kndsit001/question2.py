hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))
if(-1<hours<24 and -1<minutes<60 and -1<seconds<60):
    print("Your time is valid.")
else:
    print("Your time is invalid.")