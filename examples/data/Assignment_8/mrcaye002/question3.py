#Recursive program to encrypt a message by converting all lowercase characters to the next character
#Ayesha Marcus
#06/05/2014

import math

def main ():
  sInput = "" 
  print ("Enter a message:")
  sInput=input("")
  print ("Encrypted message:")
  convertChar (sInput, 0, 0)
 
def convertChar (sVal, iPos, iCnt):
#a=97
#z=122
#A=65
#Z=90
  #if(len(sVal)-1>=iPos):
  #  return
    
  ordVal=ord(sVal[iPos])
  charVal=ordVal
  #if(ordVal>64 and ordVal<91):
  #  if(ordVal==90):
  #    charVal=64
  #  charVal = charVal + 1
  if(ordVal>96 and ordVal<123):
    if(ordVal==122):
      charVal=96
    charVal = charVal + 1

  print(chr(charVal), end="")    
  #print(ord(sVal[iPos]))  
  iPos = iPos + 1

  if(iPos > (len(sVal)-1)):
    return

  convertChar (sVal, iPos, iCnt)
  return
  
if __name__ == "__main__":
   main()
