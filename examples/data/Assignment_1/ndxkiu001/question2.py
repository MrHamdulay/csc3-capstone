h,m,s = eval(input("Enter the hours:\n")),eval(input("Enter the minutes:\n")),eval(input("Enter the seconds:\n"))

if h >= 0 and h < 24 and m >=0 and m <60 and s >= 0 and s <60:
    print ("Your time is valid.")
else:
    print("Your time is invalid.")
    
