#Program to analyse student marks (read in from a file)
#Ayesha Marcus
#12/05/2014

import math

def main ():            #Ask user for filename
  lines = []
  print ("Enter the marks filename:")
  sFile=input("")

  lines = returnFile(sFile)
  
  sVal=""
  comma=""
  iSum=0
  for i, line in enumerate(lines):
    #print(line)
    val=line.rstrip().split(',', 1 )
    iSum+=int(val[1])
    sVal=sVal+comma+str(val[1])
    comma=","
    #print(val[1])

  iAvg=round(iSum/len(lines),2)      #Calculate Average
  
  iVal=0
  for i, line in enumerate(lines):   #Calculate student mean
    #print(line)
    val=line.rstrip().split(',', 1 )
    iVal += math.pow(int(val[1])-iAvg,2)

  #print(round(math.sqrt(iVal/len(lines)),2))
  print("The average is:","%0.2f" % iAvg)
  print("The std deviation is:", "%0.2f" % round(math.sqrt(iVal/len(lines)),2))
  
  bPrintHeading=True
  fPass = iAvg-round(math.sqrt(iVal/len(lines)),2)
  for i, line in enumerate(lines):
    #print(line)
    val=line.rstrip().split(',', 1 )
    if(eval(val[1])<fPass):
      if(bPrintHeading):
        print("List of students who need to see an advisor:")        
        bPrintHeading=False
      print(val[0])
  
def returnFile (sFilename):          #Read in from a file
  with open(sFilename) as f:
    content = f.readlines()

  return content;
  
if __name__ == "__main__":
   main()

