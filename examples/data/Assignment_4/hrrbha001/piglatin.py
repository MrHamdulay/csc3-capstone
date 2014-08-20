VOWELS = ('a', 'e', 'i', 'o', 'u')
ENDS = ('y','x','k','s')

def toEnglish (s):
   list_of_words = s.split(' ')
   new_sentence = ""   
   for word in list_of_words:
      new_sentence = new_sentence + convert_word_e(word)    
      new_sentence = new_sentence + " "   
   return new_sentence

def convert_word_e(word):
   index= len(word)-3
   last_three = word[index:]
   #print(last_three, end=" ")
   if last_three == "way":  
      return word[:index]     
   else:
      index2 = len(word)-2
      temp = word[:index2]
      t_len = len(temp)
      if (temp[t_len-1] in VOWELS) or (temp[t_len-2] in ENDS):
         return temp[t_len-1]+temp[:t_len-1] 
      else:
         return temp[t_len-2]+ temp[t_len-1]+temp[:t_len-2] 
      
def to_english(word):
   if word[-3:] == "way":
      if word.find('-') != -1:
         return word[word.find('-') + 1 : -3] + word[: word.find('-')].lower()
      else:
         return word[:-3].lower()
   elif (word[-2 : ] == "ay"):
      if word.find('-') != -1:
         return word[word.find('-') + 1 : -2] + word[: word.find('-')].lower()
      else:
         return word[ : -2].lower()
               
   
def convert_word(word):
   first_letter = word[0]
   if first_letter in VOWELS:  
      return word + "way"     
   else: 
      for j in range (0, len(word)):
         if word[j] in VOWELS:
            index=j
      return word[index:] + word[:index] + "ay"   
                                            
def toPigLatin(s):
   list_of_words = s.split(' ')
   new_sentence = ""   
   for word in list_of_words:
      new_sentence = new_sentence + convert_word(word)    
      new_sentence = new_sentence + " "   
   return new_sentence


#text = input("Enter:")  # nothing in the parentheses, because there's nothing else
                    # extra to tell the user before he is allowed to type


#print (convert_sentence(text))