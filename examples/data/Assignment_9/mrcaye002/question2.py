#Program to reformat a text file so that all lines are at most a given length.
#Ayesha Marcus
#12/05/2014

import math

def main ():
  lines = []                 # Initialize lists
  allWords = []
  print ("Enter the input filename:")
  sFile=input("")                            #Ask user for input filename
  #sFile="input.txt"
  print ("Enter the output filename:")       #Ask user for output filename
  sOutFile=input("")
  #sOutFile="output.txt"
  
  print ("Enter the line width:")
  iLineWidth=eval(input(""))
  #iLineWidth=20
  
  fo=open(sOutFile,"w")                #Open file to overwrite
  fo.close()
  lines = returnFile(sFile)
  for i, line in enumerate(lines):
    for word in line.split():
      allWords.append(word)
  
  for i, line in enumerate(allWords):
    allWords[i] = allWords[i].replace("`BLANK`","\n").replace('`$`',' ')

  iPos = 0
  while iPos != -1:
    iPos = printLength(allWords, iLineWidth, iPos, sOutFile)

  
def printLength(words, iLen, iStart, strFile):         #Calculate length 
  iCnt = 0
  strLine=""
  space = ""
  while iCnt != -1:
    if(iStart>=len(words)):
      iStart = -1
      iCnt = -1
      break
    if(words[iStart] in ('\n','\r\n')):
      iCnt = -1
      strLine += (words[iStart])
      iStart = iStart + 1
      break
    if(len(words[iStart]) + iCnt > (iLen-1)):
      iCnt = -1
      break
    if(len(words[iStart]) + iCnt <= (iLen-1)):
      strLine += (space + words[iStart])
      space = " "
      iStart = iStart + 1
      iCnt = len(strLine)
  if(len(strLine) > 0):
    if(iStart==-1):
      writeToFile(strFile, strLine)
    else:
      writeToFile(strFile, strLine + "\n")
  #print(strLine, len(strLine))
  return iStart

def writeToFile(sFileName, sLine):                 #Append file 
  with open(sFileName, "a") as myfile:
    myfile.write(sLine)



def returnFile (sFilename):
  content = []
  f = open(sFilename)
  for line in f:
     if line in ['\n', '\r\n']:
       content.append("`BLANK`")
     else:
       content.append(line.replace('  ',' `$`'))
  #with open(sFilename) as f:
  #  content = f.readlines()
    
  #for i, val in enumerate(content):
  #  content[i] = content[i].replace('  ',' `$`')
  #content = content.replace('  ',' `$`')
  return content;
  
if __name__ == "__main__":
   main()

