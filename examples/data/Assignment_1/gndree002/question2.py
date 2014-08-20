hours = eval(input("Enter the hours:\n"))
minu = eval(input("Enter the minutes:\n"))
sec = eval(input("Enter the seconds:\n"))
if(hours>=0) & (hours<=23) & (minu>=0) &(minu<=60) & (sec>=0) & (sec<=60):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
