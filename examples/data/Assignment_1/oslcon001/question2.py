hour = eval(input("Enter the hours:\n"))
mins = eval(input("Enter the minutes:\n"))
sec = eval(input("Enter the seconds:\n"))

if hour >= 0 and hour <= 23:
    hour = True
    
if mins >= 0 and mins <= 59:
    mins = True
    
if sec >= 0 and sec <= 59:
    sec = True
    
if hour == True and mins == True and sec == True:
    print("Your time is valid.")
else:
    print("Your time is invalid.")


           
            