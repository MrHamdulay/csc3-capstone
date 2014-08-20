def toPigLatin(v):
  d=v.split(" ")
  y=""
  for c in range(len(d)):
    dy=0
    word=d[c]
    e=word[0]
    if e in "aeiou" or e in "AEIOU":
      word+="way"
    else:
      for i in range(len(word)):
        e=word[i]
        if e in "aeiou" or e in "AEIOU":
          dy=i
        else:
          if(i+1!=len(word)):
            continue
          else:
            word="a"+word+"ay"
            break
        word=word[dy::]+"a"+word[0:dy]+"ay"
        break
    y+=word+" "
  return y      
def toEnglish(v):
  d=v.split(" ")
  y=""
  for c in range(len(d)):
    word=d[c]
    s=word[len(word)-3::]
    if(s=="way"):
      word=word[0:len(word)-3:1]
    else:
      z=0
      word=word[0:len(word)-2:1]
      for j in range(len(word)):
        if word[j] in "aeiou" or word[j] in "AEIOU":
          q=j+1
    if(s=="way"):
      y+=word+' '
    else :
      y+=word[q::]+word[0:q-1:1]+" "
  return y
        