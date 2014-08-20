vowels=('a','e','i','o','u')
def convert_word(word):
    first_letter= word[0]
    if first_letter in  vowels:
        return word+"way "
    else:
        return word[1:]+ "a" +word[0]+"ay "
    

def toPigLatin(s):
    word_list=s.split(' ')
    PigLatin=""
    for x in word_list:
        PigLatin= PigLatin+ convert_word(x)
    return PigLatin

def convert_word2(Word):
    length=len(Word) 
    if Word[length-3:length] =="way":
        new_word= Word[0:length-3]
        return new_word+" "
    else:
        first_letter=Word[length-3]
        new_word= first_letter + Word[0:length-4]
        return new_word+" "

def toEnglish(s):
    Word_list=s.split(' ')
    English=""
    for X in Word_list:
        English= English+ convert_word2(X)
    return English  
    
    

 

        


        
        
