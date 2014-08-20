def validity():
    if 0 <= h <= 24 and 0 <= m <= 59 and 0 <= s <= 59 :
        print("Your time is valid.")
    else:
        print("Your time is invalid.")
        
h = eval(input("Enter the hours: \n"))
m = eval(input("Enter the minutes: \n"))
s = eval(input("Enter the seconds: \n"))


validity()