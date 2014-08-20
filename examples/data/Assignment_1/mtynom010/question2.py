hours=eval(input("Enter the hours:\n"))
mi=eval(input("Enter the minutes:\n"))
sec=eval(input("Enter the seconds:\n"))

if 0<=hours<=23 and 0<=sec<=59 and 0<=mi<=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")