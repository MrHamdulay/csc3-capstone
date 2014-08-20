error=0
hours=eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

if (hours > 23) or (type(hours) != int):
    error=1
if hours < 0:
    error=1
if (minutes > 59) or (type(minutes) != int):
    error=1
if minutes < 0:
    error=1
if seconds > 59 or (type(seconds) != int):
    error=1
if seconds < 0:
    error=1

if error == 1:
    print("Your time is invalid.")
else:
    print("Your time is valid.")
