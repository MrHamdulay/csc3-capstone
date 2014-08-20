# program to test the validity of time
# SRGVAR001 
# Vardhani Sarugaser    
# 1 March 2014

hours = eval(input("Enter the hours:\n"))
mins = eval(input("Enter the minutes:\n"))
sec = eval(input("Enter the seconds:\n"))

if hours >= 0 and hours <=23 and mins >=0 and mins <= 59 and sec >= 0 and sec <=59 :
    print("Your time is valid.")
else :
    print("Your time is invalid.")