def toPigLatin (s): 
   fin = " "
   for j in s.split(" "):
      v = "aeiou"
      new = ""
      for i in str(j):
         if i == v[0] or i == v[1] or i == v[2] or i == v[3] or i == v[4]: break
         else: new = new + i   
      
      b = len(new)
      ay = "ay"
      a = "a"
      if b == 0: 
         ay = "way"
         a = ""
      j = j[b:] + a + new + ay
      fin = fin + j + " "

   return(fin[1:])

def toEnglish (s):
   word = ""
   iii = ""
   for i in s.split(" "):
    
    
      ii = i[::-1]
    
      if ii[2] == "w": 
         iii = ii[3:]
         word = word + iii[::-1] + " "
      else: 
         iii = ii[2:]
         count = 0
         for j in range(len(iii)):
            
            k = str(iii[j])
            if k != "a": 
               count = count + 1
            if k == "a": 
               break
         word = word + ((iii[:count])[::-1]) + ((iii[count + 1:])[::-1]) + " "
   return word


 
 
 
