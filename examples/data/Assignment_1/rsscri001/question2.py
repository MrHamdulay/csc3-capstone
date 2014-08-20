x = eval(input("Enter the hours:\n"))

y = eval(input("Enter the minutes:\n"))

z = eval(input("Enter the seconds:\n"))
if 0 <= x and x <= 23 and 0 <= y and y <= 59 and 0 <= z and z <= 59:
    print("Your time is valid.")
if x < 0 or x > 23 or y < 0 or y > 59 or z <0 or z > 59:
    print("Your time is invalid.")
    

        