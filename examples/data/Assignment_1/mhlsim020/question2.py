#Program using IF and IF-ELSE to check validity of time entered by user.
#Simlindile Mahlaba
#07 March 2014

hours=eval(input("Enter the hours: \n"))
minutes=eval(input("Enter the minutes: \n"))
seconds=eval(input("Enter the seconds: \n"))

if(0<=hours and hours<=23) and (0<=minutes and minutes<=59) and (0<=seconds and seconds<=59): 
    print("Your time is valid.")
else:
    print("Your time is invalid.")