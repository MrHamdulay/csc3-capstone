msg = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

length = (rep) + (frame*2)
breadth = ((frame * 2) + 2) + len(msg)
plusSigns = 0
i = length//2
counter = 0
lineCounter = 0
intaltantionsLengthOfHyphen = breadth
while (counter < length):
     if (counter - frame < 0):
          counter += 1
          intaltantionsLengthOfHyphen -= 2
          print(("|")*lineCounter,"+", intaltantionsLengthOfHyphen*("-"), "+", ("|")*lineCounter,sep="")
          
          lineCounter += 1
     elif ((counter + frame) >= length):
          counter += 1
          
          lineCounter -= 1
          print(("|")*lineCounter, "+", intaltantionsLengthOfHyphen*("-"), "+", ("|")*lineCounter,sep="")
          intaltantionsLengthOfHyphen += 2
          
          
     else:
          print(("|")*frame, " ", msg, " ", ("|")*frame,sep="")
          counter += 1
     
                        
          
          
          
      