#question_2
#Thrianka Naidoo
#NDXTHR005

hour = int(input("Enter the hours: \n"))
minute = int(input("Enter the minutes: \n"))
seconds = int(input ("Enter the seconds: \n"))

if (hour<=23 and hour>=0):
       
       if (minute<=59 and minute>=0):
              
              if (seconds<=59 and seconds>=0):
                     
                     print("Your time is valid.")
                     
              else:
                     print("Your time is invalid.")
       else:
              print("Your time is invalid.")
else:
       print("Your time is invalid.")