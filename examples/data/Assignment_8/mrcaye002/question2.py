#Recursive program to count the number of pairs of repeated characters in a string
#Ayesha Marcus
#06/05/2014

import math

def main ():
  sInput = "" 
  print ("Enter a message:")
  sInput=input("")
  checkPairs (sInput, 0, 0)
 
def checkPairs (sVal, iPos, iCnt):
  if(iPos >= len(sVal)-1):
    print("Number of pairs:", iCnt)
    return
  if(sVal[iPos]==sVal[iPos+1]):
    iCnt=iCnt+1
    iPos=iPos+1
  
  iPos=iPos+1  
  checkPairs(sVal, iPos, iCnt)
  
  return
  
if __name__ == "__main__":
   main()
