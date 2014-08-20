def toPigLatin(s):
   
   string=""
   
   for word in s.split(' '):
      
      if (word[0] in "aeiou"):
         string+=word+"way "
         
      else:         
         for pos in range(len(word)):
            if (word[pos] in "AEIOUaeiou"):
               vowel=pos
               break
            
         string+=word[pos:]+word[0:pos]+"ay "
         
   return string[:-1]


def toEnglish(s):
   string=""
   
   for word in s.split(' '):
      
      if "w" in word:
         string+=word[:-3]+' '
      
      elif (word[-4:-2] in "sh ph bl br ch cl cr dr fl fr gl gr pl pr sc sh sk sl sm sn sp st th tr"):
         string+=word[-4:-2]+word[:-4]+" "
            
      elif (word[-5:-2] in "sch scr shr sph spl spr squ str thr"):
         string+=word[-5:-2]+word[:-5]+" "
            
      else:
         string+=word[-3]+word[:-3]+" "
         
            
   return string[:-1]