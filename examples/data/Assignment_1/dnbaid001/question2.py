#Programme to check date input validity
#Aidan de Nobrega
#DNBAID001
#25/02/2014

def datevalid():
   hours = eval(input("Enter the hours:\n")) #\n allows new-line input
   minutes = eval(input("Enter the minutes:\n"))
   seconds = eval(input("Enter the seconds:\n"))
   
   if hours >= 0 and hours <= 23 and minutes >= 0 and minutes <= 59 and seconds >= 0 and seconds <= 59:
      print ("Your time is valid.") #all variables inclusive in one if/else statement
      
   else:
      print ("Your time is invalid.")

datevalid()
   
   
    

    