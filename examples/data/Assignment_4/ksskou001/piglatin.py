#Name: Kouame KOUASSI
#Student_Number: KSSKOU001
#Date: 31-03-2014
#Assignment_4
#Question3_piglatin to english and vis-versa = 'string' and def functions():

def toPigLatin(s):
 
   '''This function returns a string containing the thanslation
   of a given english word into piglatin'''
   
   import string 
   c = 0
   piglatin_s = ''
   piglatin_w = ''
   word = ''
   a = 0
   s += ' '
   for i in s:
      if i == ' ':
         word = s[a:c]
         if word[0] in 'aeiou':
            piglatin_w = word + 'way' + ' '
       
         else:
            c2 = 0
            for i in word:
               if i in 'aeiou':
                  piglatin_w = word[c2:] + 'a' + word[:c2] + 'ay' + ' '
                  break
               elif word.find('a') == -1 and word.find('e') == -1 and word.find('i') == -1 and word.find('o') == -1 and word.find('u') == -1 and i == word[len(word)-1]:
                  piglatin_w = 'a' + word[:] + 'ay' + ' '
               else:
                  c2 += 1
                  continue
         piglatin_s += piglatin_w        
         a += len(word) + 1
         c += 1
      else:
         c += 1
         continue
   piglatin_s = piglatin_s[:len(piglatin_s)-1] 
   return piglatin_s



def toEnglish(s): 
   c = 0
   english_s = ''
   english_w = ''
   word = ''
   a = 0
   s += ' '
   for i in s:
      if i == ' ':
         word = s[a:c]
         if word[len(word)-3:] == 'way':
            english_w = word[:len(word)-3] + ' '
         elif word[len(word)-2:] == 'ay':
            word = word[:len(word)-2]
            c2 = 0
            for i in word[::-1]:
               if i == 'a':
                  english_w = word[len(word)-c2:] + word[:len(word)-c2-1] + ' '
                  word += 'ay' 
                  break
               else:
                  c2 += 1
                  continue
         english_s += english_w
         a += len(word) + 1
         c += 1
      else:
         c += 1
         continue
      
   english_s = english_s[:len(english_s)-1]
   return english_s