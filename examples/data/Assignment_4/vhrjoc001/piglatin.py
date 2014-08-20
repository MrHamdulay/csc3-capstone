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
               vowel=0
         if vowel==0:
            string+="a"+word+"ay "
         else:
            string+=word[vowel:]+"a"+word[0:vowel]+"ay "
         
   return string[:-1]


def toEnglish (s):
      string=""
      
      for word in s.split(' '):
         if "w" in word:
            string+=word[:-3]+' '
         else:
            word=word[:-2]
            for pos in range(len(word)-1,-1,-1):
               if word[pos]=='a':
                  break
            if pos!=(len(word)+1) or len(word)==3:
               string+=word[pos+1:]+word[:pos]+' '
            elif word=="eath":
               string+="the "
            else:
               string+=word[1:]+" "
                
              
             
      return string[:-1]