#Program to print a list of strings entered, in the same order but without duplicates.
#Ayesha Marcus
#30/04/2014

def main ():
  sInput = ""                                 #Empty string
  words = []                                  #Empty list
  uniqueWords = []
  iMaxLength = 0                              #Initialise counter
  print ("Enter strings (end with DONE):")
  while sInput != "DONE":                     #Sentinel DONE
    sInput=input("")
    words.append(sInput)                      #Add words to string
  else:
    print("")
    
  print("Unique list:")              
  for i in range(len(words)):
    if (words[i] != "DONE"):
      if exists(uniqueWords, words[i]) == 0:
        uniqueWords.append(words[i])
      
  for i in range(len(uniqueWords)):            #Print unique list 
    print(uniqueWords[i]) 
    

 
def exists (vList, sVal):
  yesNo = 0
  for i in range(len(vList)):
    if (vList[i] == sVal):
      yesNo = 1
      break
      
  return yesNo;
  
if __name__ == "__main__":
   main()
