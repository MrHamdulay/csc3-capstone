#Question2
#name: Hannah Frank
#student number: FRNHAN004
#date: 1 March 2014

hours = int(input("Enter the hours:\n"))
minutes = int(input("Enter the minutes:\n"))
seconds = int(input("Enter the seconds:\n"))

if 0 <= (hours) <= 23 and 0 <= (minutes) <= 59 and 0 <= (seconds) <= 59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")

