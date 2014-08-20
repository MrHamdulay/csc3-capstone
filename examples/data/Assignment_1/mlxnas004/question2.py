# program to check the validity of time entered by user
# nasha meoli
# 25 february 2014
# create valid_hours in program

valid_hours =  24                # create valid_hours in program

hours = 0                       # variable to store user's input

valid_minutes =  60      # create valid_minutes in program

minutes = 0                     # variable to store user's input

valid_seconds = 60     # create valid_seconds in program

seconds = 0                     # variable to store user's input 

#get input from user

hours = eval (input ("Enter the hours:\n"))

minutes = eval (input ("Enter the minutes:\n"))

seconds = eval (input ("Enter the seconds:\n"))

   
# while input is valid
if (hours < valid_hours and hours >= 0) and (minutes < valid_minutes and minutes >= 0) and (seconds < valid_seconds and seconds >= 0): 
    print ("Your time is valid.")
else:
    print ("Your time is invalid.") 
    

    



    


