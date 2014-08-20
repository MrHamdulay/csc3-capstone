#Cherise Dube
#04 April 2014
"""Program to convert to pig latin and back"""

vowels=['a','e','i','o','u']
def convert_word (word):    #Converts English words into Piglatin
    if word[0] in vowels:
        return word+"way"
    elif word[0]not in vowels and word[1] not in vowels and word[2] not in vowels:
        return word[3:]+"a"+word[0:3]+"ay"
    
    elif word[0] not in vowels and word[1] not in vowels:
        return word[2:]+"a"+word[0:2]+"ay" 
    
    elif word[0] not in vowels:
        return word[1:]+"a"+word[0]+"ay"
    
def toPigLatin (s): #Makes a full Piglatin sentence
    ind_words=s.split(" ")
    new_sentence=""
    new_word=""
    for i in (ind_words):
        new_word=convert_word(i)
        new_sentence=new_sentence+new_word+" "
    return new_sentence

def convert_word2 (word):   #Converts Piglatin words into English
    new_word=word[0:-2]
    if word[-3:]=="way":
        return word[0:-3]
    if new_word[-1] not in vowels and new_word[-2] not in vowels and new_word[-3] not in vowels:
        return new_word[-3:]+new_word[0:-4]
    if new_word[-1] not in vowels and new_word[-2] not in vowels:
        return new_word[-2:]+new_word[0:-3]
    if new_word[-1] not in vowels:
        return new_word[-1]+new_word[0:-2]

def toEnglish (s):  #Converts Piglatin sentence into English
    ind_words=s.split(" ")
    new_sentence=""
    new_word=""
    for i in (ind_words):
        new_word=convert_word2(i)
        new_sentence=new_sentence+new_word+" "
    return new_sentence
       
    
    
  
    
