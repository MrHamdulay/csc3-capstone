hour = 0
minute = 0
second = 0
count = 0
hour = eval(input("Enter the hours:\n"))
minute = eval(input("Enter the minutes:\n"))
second = eval(input("Enter the seconds:\n"))
if hour > 23:
    count = 5
if minute > 59:
    count = 5
if second > 59:
    count = 5
if hour < 0:
    count = 5
if minute < 0:
    count = 5
if second < 0:
    count = 5
if count < 1:
    print("Your time is valid.")
if count > 2:
    print("Your time is invalid.")    

    