#Jade Petersen
#Assignment1_question2
#7 March 2014

hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))

def time(hours,minutes,seconds):
   if (0<=hours<=23 and 0<=minutes<=59 and 0<=seconds<=59):
            print("Your time is valid.")
   else:
      print("Your time is invalid.")
      
time(hours,minutes,seconds)