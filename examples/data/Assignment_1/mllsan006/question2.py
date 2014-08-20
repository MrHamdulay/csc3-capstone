hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
secondes = eval(input("Enter the seconds:\n"))

if 0<=hours<=23 and 0<=minutes<=59 and 0<=secondes<=59:
    print("Your time is valid.")
    
else:
    print("Your time is invalid.")
    