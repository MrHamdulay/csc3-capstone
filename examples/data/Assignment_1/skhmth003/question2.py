x = int(input("Enter the hours:\n"))
y=int(input("Enter the minutes:\n"))
z=int(input("Enter the seconds:\n"))
if x in range(0, 24) and y in range(0, 60) and z in range (0, 60):
 Bad = 0
else:
 Bad = 1
if Bad ==1:
 print("Your time is invalid.")
else:
 print("Your time is valid.")
