hrs=eval(input("Enter the hours:\n"))
min=eval(input("Enter the minutes:\n"))
sec=eval(input("Enter the seconds:\n"))

if 0 <= hrs <= 24 and 0 <= min <= 60 and 0 <= sec <= 59:
    print("Your time is valid.")
    
else:
    print("Your time is invalid.")
   