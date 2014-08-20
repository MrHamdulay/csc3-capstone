#Author: C.Longmore
#Date: 28 February2014
hours=input("Enter the hours:""\n")
minutes=input("Enter the minutes:""\n")
seconds=input("Enter the seconds:""\n")
hours=eval(hours) #change string into number
minutes=eval(minutes)
seconds=eval(seconds)
if (0<=hours<=23) and (0<=minutes<=59) and (0<=seconds<=59):
    print("Your time is valid.")
else: print("Your time is invalid.")

