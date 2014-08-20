h= eval(input("Enter the hours:\n"))
m= eval(input("Enter the minutes:\n"))
s= eval(input("Enter the seconds:\n"))
if (h in range(24)) and (m in range(60)) and ( s in range(60)):
    print("Your time is valid.")
    
else:
    print("Your time is invalid.")
    
    
