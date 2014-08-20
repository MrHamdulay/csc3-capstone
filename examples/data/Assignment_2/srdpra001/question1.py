"""
SRDPRA001
Assignment 2
Question 1
"""
def LYear(year):
	 if((year % 4) == 0):
		  if((year % 100) == 0):
			   if( (year % 400) == 0):
				    return 1
			   else:
				    return 0
	 
	 else:
		  return 0
	 return 1
      
i = 0
print ("Enter a year: "), 
i = eval(input())
if(LYear(i) == 0):
	 print (i, "is not a leap year.")
else:
	 print (i, "is a leap year.")
	 