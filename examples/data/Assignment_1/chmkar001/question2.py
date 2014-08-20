#Program to check the validity of time entered.
#Modi Pascaline Antoinette Komana
#KMNMOD001
#February 2014


hours = input("Enter the hours:\n")
minutes = input("Enter the minutes:\n")
seconds = input("Enter the seconds:\n")
hours = int(eval(hours))
minutes = int(eval(minutes))
seconds = int(eval(seconds))
if (0<=hours<=23) and (0<=minutes<=59) and (0<=seconds<=59):
   print ("Your time is valid.")
    
else : print ("Your time is invalid.")
    