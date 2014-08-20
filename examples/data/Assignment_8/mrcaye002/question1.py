#Recursive program to calculate whether or not a string is a palindrome
#Ayesha Marcus
#06/05/2014

import math

def main ():
  sInput = "" 
  print ("Enter a string:")
  sInput=input("")
  palindrome (sInput, 0)
 
def palindrome (sVal, iPos):
  iStop = math.floor(len(sVal)/2)
  if(iPos > iStop):
    print ("Palindrome!")
    return
  	
  if (iPos <= iStop):
  	if(sVal[iPos]!=sVal[len(sVal)-(iPos+1)]):
  	  print("Not a palindrome!")
  	if(sVal[iPos]==sVal[len(sVal)-(iPos+1)]):
  	  palindrome(sVal, iPos+1)
  return;
  
if __name__ == "__main__":
   main()
