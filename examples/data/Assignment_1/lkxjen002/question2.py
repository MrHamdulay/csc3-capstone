# validity.py
#    A program to check the validity of time entered by user
# Author: Jenna Lake
# date: 25 Feburary 2014

hours = input ("Enter the hours: \n")
minutes = input ("Enter the minutes: \n")
seconds = input ("Enter the seconds: \n")
hours=eval(hours)   #change string into number
minutes=eval(minutes)
seconds=eval(seconds)
    
#Print assessment of validity of time entered
if 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
   print ("Your time is valid.")
else:
   print ("Your time is invalid.")