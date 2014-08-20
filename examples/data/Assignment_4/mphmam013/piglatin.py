def toPigLatin(v):
  m=v.split(" ")
  x=""
  for l in range(len(m)):
    mx=0
    word=m[l]
    n=word[0]
    if n in "aeiou" or n in "AEIOU":
      word+="way"
    else:
      for i in range(len(word)):
        n=word[i]
        if n in "aeiou" or n in "AEIOU":
          mx=i
        else:
          if(i+1!=len(word)):
            continue
          else:
            word="a"+word+"ay"
            break
        word=word[mx::]+"a"+word[0:mx]+"ay"
        break
    x+=word+" "
  return x       
def toEnglish(v):
  m=v.split(" ")
  x=""
  for l in range(len(m)):
    word=m[l]
    s=word[len(word)-3::]
    if(s=="way"):
      word=word[0:len(word)-3:1]
    else:
      z=0
      word=word[0:len(word)-2:1]
      for i in range(len(word)):
        if word[i] in "aeiou" or word[i] in "AEIOU":
          z=i+1
    if(s=="way"):
      x+=word+' '
    else :
      x+=word[z::]+word[0:z-1:1]+" "
  return x
        