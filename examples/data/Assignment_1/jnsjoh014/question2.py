#Johan Jansen van Vuuren
#JNSJOH014
#Assignment 1 Question 2

def userInput():
   
   #initialise variables
   hValid = True
   mValid = True
   sValid = True
   
   hours =   eval(input("Enter the hours:\n"))
   #Validate hours   
   if (hours>=24 or hours<0):
     hValid = False
      
   minutes = eval(input("Enter the minutes:\n"))
   
   #Validate minutes   
   if(minutes>=60 or minutes<0):
      mValid = False
        
   seconds = eval(input("Enter the seconds:\n"))
   #Validate seconds
   if(seconds>=60 or seconds<0):
      sValid = False
      
   if(hValid and mValid and sValid):
      print("Your time is valid.")
   else:
      print("Your time is invalid.")
   
userInput()