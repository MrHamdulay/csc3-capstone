VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def consonant_check(a):
 first = a.lower()
 if first in ('a', 'e', 'i', 'o', 'u'):
  return False
         
 else:
  return True

  
def conv_consonant_start(word):
 if len(word)>=2 and consonant_check(word[1]) == True:
  if len(word)>=3 and consonant_check(word[2]) == True:
   if len(word)>=4 and consonant_check(word[3]) == True:
    pig_latin_word = word[4:] + "a" + word[0:4] + "ay"
   else:
    pig_latin_word = word[3:] + "a" + word[0:3] + "ay"
  else:
   pig_latin_word = word[2:]+ "a" + word[0:2] + "ay" 
 else:
  pig_latin_word = word[1:]+ "a" + word[0] + "ay" 
 
 return pig_latin_word
 
def conv_vowel_start(word):
 pig_latin_word = word + "way"
 return pig_latin_word
 
def toPigLatin(s):
 engl_words = s.split(" ")
 
 pig_latin_words = []
 
 for i in engl_words:
  first_letter = i[0]
  vowel = False
  if first_letter in VOWELS:
   vowel = True
  if vowel == True:
   pig_latin_words.append(conv_vowel_start(i))
  else:
   pig_latin_words.append(conv_consonant_start(i))
 
 new = " ".join(pig_latin_words)
 return new

def toEnglish(s):
 pigl_words = s.split(" ")
 
 eng_words = []
 
 for i in pigl_words:
  three_last = i[-3:-1]
  if three_last == "wa":
   eng_words.append(vowel(i))
  else:
   eng_words.append(cons(i))
 
 neweng = " ".join(eng_words)   
 return neweng
    
    
    
    
def vowel(word):
 word = word[:(len(word)-3)]
 return word

def cons(word):
 word = word[:(len(word)-2)]
 #if len(word)>2 and consonant_check(word[-2]) == True:
 a = word.rfind("a")
 last = word[a+1:]
 word = word[0:a]
 engword = last + word
 #else:
  #last = word[-1]
  #word = word[0:len(word)]  
  #engword = last + word                           
  
 return engword

