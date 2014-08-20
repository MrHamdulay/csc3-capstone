def toPigLatin(sen):
  listS=sen.split(" ")
  s=""
  for l in range(len(listS)):
    stopI=0
    cWord=listS[l]
    fChar=cWord[0]
    if fChar in "aeiou" or fChar in "AEIOU":
      cWord+="way"
    else:
      for i in range(len(cWord)):
        fChar=cWord[i]
        if fChar in "aeiou" or fChar in "AEIOU":
          stopI=i
        else:
          if(i+1!=len(cWord)):
            continue
          else:
            cWord="a"+cWord+"ay"
            break
        cWord=cWord[stopI::]+"a"+cWord[0:stopI]+"ay"
        break
    s+=cWord+" "
  return s       
def toEnglish(sen):
  listS=sen.split(" ")
  s=""
  for l in range(len(listS)):
    cWord=listS[l]
    last=cWord[len(cWord)-3::]
    if(last=="way"):
      cWord=cWord[0:len(cWord)-3:1]
    else:
      lc=0
      cWord=cWord[0:len(cWord)-2:1]
      for i in range(len(cWord)):
        if cWord[i] in "aeiou" or cWord[i] in "AEIOU":
          lc=i+1
    if(last=="way"):
      s+=cWord+' '
    else :
      s+=cWord[lc::]+cWord[0:lc-1:1]+" "
  return s
        