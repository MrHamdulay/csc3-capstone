#Tejasvin Bagirathi
#Assignment 4, Question 3

def toPigLatin(s):
   wrdno = 1
   new = ""
   for i in range(len(s)):
      if s[i] == " ":
         wrdno+=1
   string = s.split(" ")
   for i in range(wrdno):
      wrd = string[i]
      #If word starts with vowel
      if wrd[0] in "aeiou":
         wrd = wrd + "way"
         if wrdno == i:
            new += wrd
         else: 
            new += wrd + " "         
      else:
         k = 0
         for c in wrd[:]:
            if c not in "aeiou":
               k+=1
            else: break
         wrd = wrd[k:len(wrd)] + "a" + wrd[0:k] + "ay"
         if wrdno == i:
            new += wrd
         else: 
            new += wrd + " "
   
   return new
         
def toEnglish(s):
   sentence=s.split()
   newsentence=""
   for word in range(len(sentence)):
         if sentence[word][-3:]=="way":
            newsentence+=sentence[word][:-3]+" "
         elif sentence[word][-2:]=="ay":
            nWord=sentence[word][:-2]
            aPos=nWord.rfind("a")
            newsentence+=nWord[aPos+1:]+nWord[:aPos]+" "
      
   return(newsentence)   
   
         
         