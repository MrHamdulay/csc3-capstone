"""Dumisani Ngwenza
02/04/14
NGWDUM005"""

def toPigLatin(s):
  """Returns the Pig Latin string for a given English string"""
  word = s
  #word = "the quick black fox jumps over the lazy apple"
  empty =' '
  space_find = word.find(' ')
  count = word.count(empty)+1
  lay = " "
  new_word = ""
  while count>1:
    lay = word[:space_find]
    word = word[space_find+1:]
    if (lay[:1]== "a") or (lay[:1]=="e") or (lay[:1]=="i") or (lay[:1]=="o") or (lay[:1]=="u"):
        lay += "way"
        new_word += lay + ' ' 
    elif (lay[1:2] == "a") or (lay[1:2]=="e") or (lay[1:2]=="i") or (lay[1:2]=="o") or (lay[1:2]=="u"):
      lay = lay[1:] + "a" + lay[:1] + "ay" + ' '
      new_word += lay   
    elif (lay[2:3] == "a") or (lay[2:3]=="e") or (lay[2:3]=="i") or (lay[2:3]=="o") or (lay[2:3]=="u"):
      lay = lay[2:] + "a" + lay[:2] + "ay" + ' '
      new_word+= lay
    #elif (lay[3:4] == "a") or (lay[3:4]=="e") or (lay[3:4]=="i") or (lay[3:4]=="o") or (lay[3:4]=="u"):
      #lay = lay[3:] + "a" + lay[3:] + "ay"
      #new_word+= lay   
    #else:
      #lay = "a" + lay[:] + "ay"
      #new_word+=lay      
    count-=1
    space_find = word.find(' ')
  else:
    lay = word
    #if (lay[:1]== "a") or (lay[:1]=="e") or (lay[:1]=="i") or (lay[:1]=="o") or (lay[:1]=="u"):
            #lay += "way"
            #new_word += lay + ' '
    #elif (lay[1:2] == "a") or (lay[1:2]=="e") or (lay[1:2]=="i") or (lay[1:2]=="o") or (lay[1:2]=="u"):
            #lay = lay[1:] + "a" + lay[:1] + "ay" + ' '
            #new_word += lay
    #elif (lay[2:3] == "a") or (lay[2:3]=="e") or (lay[2:3]=="i") or (lay[2:3]=="o") or (lay[2:3]=="u"):
            #lay = lay[2:] + "a" + lay[:2] + "ay" + ' '
            #new_word+= lay  
    #elif (lay[3:4] == "a") or (lay[3:4]=="e") or (lay[3:4]=="i") or (lay[3:4]=="o") or (lay[3:4]=="u"):
            #lay = lay[3:] + "a" + lay[3:] + "ay"
            #new_word+= lay
    lay = "a" + lay[:] + "ay"
    new_word+=lay
  print (new_word)


def toEnglish(s):
  """Returns the English string for a given Pig Latin string"""
  word = s
  space_find = word.find(' ')
  count = word.count(' ')+1
  temp = " "
  new_sentence = ""  
  while count >1:
    temp = word[:space_find]
    word = word[space_find+1:]  
    #print(temp)
    
    ay_find = temp.find("ay")
    way_find = temp.find("way")
    length = int(len(temp))
    if temp[way_find:] == 'way':
      temp = temp[:way_find]
      new_sentence += temp + ' '
    else:
      temp = temp[:ay_find]
      far_right = temp.rfind('a')
      temp = temp[far_right+1:] + temp[:far_right]
      new_sentence += temp + ' '
    count-=1
    space_find = word.find(' ')  
    
  else:
    temp = word
    length = int(len(temp))
    way_find = temp.find("way")
    if temp[way_find:] == 'way':
          temp = temp[:way_find] 
          new_sentence += temp + ' '
    else:
          temp = temp[:ay_find]
          far_right = temp.rfind('a')
          temp = temp[far_right+1:] + temp[:far_right]
          new_sentence += temp + ' '    
  return new_sentence
  
  
if __name__ == "__main__":
  toPigLatin("the quick black fox jumps over the lazy apple")
  toEnglish("eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway")
  toEnglish("elloaHay orldaWay")
  toEnglish("appyahay eggsway")
  toPigLatin("a b")
  toPigLatin("aa ab ba bb")
  toEnglish("aaway abway aabay abbay")
  toPigLatin("aaaa aaab aaba aabb abaa abab abba abbb baaa baab baba babb bbaa bbab bbba bbbb")