#Program where the user can enter a list of strings
#Ayesha Marcus
#22/04/2014

def main ():
  sInput = ""                                #Empty string
  words = []                                 #Empty list
  iMaxLength = 0
  print ("Enter strings (end with DONE):")   #Sentinel "DONE"
  while sInput != "DONE":
    sInput=input("")                         #Add a string to the list 
    if (sInput != "DONE"):
      if (len(sInput) > iMaxLength):         #If length input> max length
        iMaxLength = len(sInput)             #Make length of input = max length
      words.append(sInput)
  else:
    print("")
    
  print("Right-aligned list:")
  #for i in range(len(words)):
  #  print(words[i].rjust(iMaxLength))
  
  for s in words:
    print (s.rjust(iMaxLength))
  
if __name__ == "__main__":
   main()
