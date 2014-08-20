"""Program to simulate a vending machine and calculate change
Ayesha Marcus
15/04/2014"""

import math


def getChange( change, denomination, denominationLabel ):
	#deduct denomination from change   250 in
	val=math.floor(change/denomination)  # = 200
	# if cash deducted display it
	if val > 0:
		print (val,denominationLabel)
  #return left over change
	retVal = change - (val*denomination)  # equal 50 to be returned

	return retVal;

def question2():

  stop = 1
  pay=0

  print ("Enter the cost (in cents):")
  cost=eval(input(""))

  while stop == 1:
    
    if pay < cost:
      print ("Deposit a coin or note (in cents):")
      newVal=eval(input(""))
      pay=newVal+pay
    else:
      stop=0      
      
  else:
    totalChange=0
    

  if pay > cost:
    print ("Your change is:")    
    totalChange=pay-cost
  # totalChange = getChange(250, 100, " x $1") --> 50
  totalChange = getChange(totalChange, 100, "x $1") 
  # totalChange = getChange(50, 25, "x 25") --> 0
  totalChange = getChange(totalChange, 25, "x 25c") 
  totalChange = getChange(totalChange, 10, "x 10c") 
  totalChange = getChange(totalChange, 5, "x 5c") 
  totalChange = getChange(totalChange, 1, "x 1c")
		
question2()
