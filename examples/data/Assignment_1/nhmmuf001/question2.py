# title: question2.py
# author: mufudzi nhamoinesu
# program to check the validity of a time entered by a user for three different intergers 

hours = eval(input("Enter the hours: \n"))
mins = eval(input("Enter the minutes: \n"))
secs = eval(input("Enter the seconds: \n"))

if 0<= hours <=23 and 0<= mins <=59 and 0<= secs <=59:
    print("Your time is valid.")
else:
    print("Your time is invalid.")

