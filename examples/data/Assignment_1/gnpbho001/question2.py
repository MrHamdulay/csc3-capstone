h =eval(input("Enter the hours:\n"))
m =eval(input("Enter the minutes:\n"))
s = eval(input("Enter the seconds:\n"))
if (0<=h<=23)and(0<=m<60)and(0<=s<60):
    print("Your time is valid.")
else :
    print ("Your time is invalid.")
    