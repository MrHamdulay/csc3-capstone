#Sphiwe Muthembi
#Student number : MTHSPH007
#Date : 25/02/2014
#A program to test the inputs of a user.

hours= eval(input("Enter the hours:\n"))
minutes= eval(input("Enter the minutes:\n"))
seconds= eval(input("Enter the seconds:\n"))

 #checking if hours are correct
if (hours >= 0 and hours <= 23) and (minutes >= 0 and minutes <= 59) and (seconds >= 0 and seconds <= 59) :
       print("Your time is valid.\n")
      # hours= eval(input("Enter the hours:\n"))
       

                   #check the minutes
#       print("Your time is invalid.\n")
   # minutes= eval(input("Enter the minutes:\n"))
     
       #check seconds
                 
#       print("Your time is invalid.\n")
       #seconds= eval(input("Enter the seconds:\n"))       
   
else:
       #if all inputs are correct make the following output
       print("Your time is invalid.\n")
       
#print("The time is" ,hours,minutes,seconds, sep=":")