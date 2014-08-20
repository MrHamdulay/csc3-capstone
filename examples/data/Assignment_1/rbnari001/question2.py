hour = eval(input ("Enter the hours: \n"))
minute = eval(input ("Enter the minutes: \n"))
sec = eval(input ("Enter the seconds: \n"))

if hour >= 0 and hour <= 23 and minute >= 0 and minute <= 59 and sec >= 0 and sec <= 59:
 print("Your time is valid.")
else:
    print("Your time is invalid.")