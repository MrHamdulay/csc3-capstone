# This program checks the validity of the input entered by the user
# The input has to be a set of 3 integers maximum
# Hours should be between 0 and 23 (inclusive)
# Minutes should be between 0 and 59 (inclusive)
# Seconds should be between 0 and 59 (inclusive)

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 05 March 2014

valid1 = 0
valid2 = 0
valid3 = 0

hours = eval(input("Enter the hours:\n"))

minutes = eval(input("Enter the minutes:\n"))

seconds = eval(input("Enter the seconds:\n"))


if (hours>=0) and (hours<=23):
          valid1 = 1
else:
          valid1 = 5
          
if (minutes>=0) and (minutes<=59):
          valid2 = 2
else:
          valid2 = 8
          
if (seconds>=0) and (seconds<=59):          
          valid3 = 3
else:
          valid3 = 9


if (valid1!=1) or (valid2!=2) or (valid3!=3):
          print("Your time is invalid.")
else:
          print("Your time is valid.")


#Sample IO

#Enter the hours:
#21
#Enter the minutes:
#7
#Enter the seconds:
#7
#Your time is valid.

#Sample I/O

#Enter the hours:
#25
#Enter the minutes:
#-7
#Enter the seconds:
#0
#Your time is invalid.

#Sample I/O

#Enter the hours:
#21
#Enter the minutes:
#7
#Enter the seconds:
#72
#Your time is invalid.
