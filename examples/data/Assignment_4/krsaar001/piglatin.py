def toPigLatin(s):
   
   string=""
   
   for word in s.split(' '):
      
      if (word[0] in "AEIOUaeiou"):
         string+=word+"way "
         
      else:         
         for pos in range(len(word)):
            if (word[pos] in "AEIOUaeiou"):
               vowel=pos
               break
            else:
               vowel=len(word)
            
         string+=word[vowel:]+"a"+word[0:vowel]+"ay "
         
   return string[:-1]


def toEnglish(s):
   
   string=""
   
   for word in s.split(' '):
      
      if "w" in word:
         string+=word[:-3]+' '
      
         
      else:
         word=word[:-2]
         
         for pos in range(-1,-len(word),-1):
            if word[pos]=='a':
               break
            else:
               pos = 0    
            
         string+=word[pos+1:]+word[:pos]+' '
         
   return string[:-1]

