valid = 'true'
hours=eval(input("Enter the hours:\n"))
if(0<=hours<=23):
      stop = 1
else:
      valid = 'false'
minutes =eval(input("Enter the minutes:\n"))
if(0<=minutes<=59):
      stop = 1
else:
      valid = 'false'
seconds=eval(input("Enter the seconds:\n"))
if(0<=seconds<=59):
      stop = 1
else:
      valid='false'

if(valid == 'true'):
      print("Your time is valid.")
else:
      print("Your time is invalid.")
