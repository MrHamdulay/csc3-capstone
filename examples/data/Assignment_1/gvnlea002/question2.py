hour= eval(input("Enter the hours:""\n"))
minutes= eval(input("Enter the minutes:""\n"))
secs= eval(input("Enter the seconds:""\n"))
if 0<=hour<=23 and 0<=minutes<=59 and 0<=secs<=59:
   print( "Your time is valid.")
else:
   print("Your time is invalid.")
   