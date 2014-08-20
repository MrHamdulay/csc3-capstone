h=eval(input("Enter the hours:\n"))
m=eval(input("Enter the minutes:\n"))
s=eval(input("Enter the seconds:\n"))
if h >= 0 and h <= 23 and m >= 0 and m <= 59 and s>=0 and s<=59:
    print("Your time is valid.")
    
else:
    print("Your time is invalid.")
    
