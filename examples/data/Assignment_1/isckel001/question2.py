#Validity of time
#Kelly Isaacs
#Date: 05-03-2014

#Creating input values for user
hours= eval(input("Enter the hours:\n"))
minutes=eval(input("Enter the minutes:\n"))
seconds=eval(input("Enter the seconds:\n"))

#Defining the input values
if 0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59:
    print("Your time is valid.")
    
else: print("Your time is invalid.")    
