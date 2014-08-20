def toPigLatin (s):
   split=s.split(" ")
   sentence=""
  
   for i in (split):
      if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="u" or i[0]=="o" or i[0]=="A" or i[0]=="E" or i[0]=="I" or i[0]=="U" or i[0]=="O":
         sentence=sentence+i+"way"+" "
        
      else:
         q=0
         for x in i:
            if x=="a" or x=="e" or x=="i" or x=="u" or x=="o" or x=="A" or x=="E" or x=="I" or x=="U" or x=="O":
               break
            q=q+1
         end=i[:q:1]
         begin=i[q::1]
         sentence=sentence+begin+"a"+end+"ay"+" "
   return sentence

def toEnglish (s): 
   split=s.split(" ")
   sentence=""
  
   for i in (split):
      end=i[-3::1]
      if end=="way":
         begin=i[:-3:1]
         sentence=sentence+begin+" "
      else:
         q=0
         for x in i[-3::-1]:
            if x=="a":
               break
            q=q+1
         begin=i[-2-q:-2:]
         end=i[0:-3-q:]
         sentence=sentence+begin+end+" "
   return sentence