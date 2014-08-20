hours = eval(input("Enter the hours:"))
print()
minutes = eval(input("Enter the minutes:"))
print()
seconds = eval(input("Enter the seconds:"))
print()
if (0<=hours<=23) and (0<=minutes<=59) and (0<=seconds<=59):
    print("Your time is valid.")
else:
    print("Your time is invalid.")
