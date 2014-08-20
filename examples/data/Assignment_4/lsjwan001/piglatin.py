def toPigLatin(s):
    end=0
    start=0
    new_sentence=""
    for i in s:
        if i==" ":
            word=s[start:end]
            new_sentence+=word_Latin(word)+" " 
            start=end+1        
        elif end==len(s)-1:
            word=s[start:]
            new_sentence+=word_Latin(word)+" "
        end+=1  
    return new_sentence
                              
def toEnglish(s):
    end=0
    start=0
    new_sentence=""
    for i in s:
        if i==" ":
            word=s[start:end]
            new_sentence+=word_English(word)+" "
            start=end+1
        
        elif end==len(s)-1:
            word=s[start:]
            new_sentence+=word_English(word)+" "
        end+=1  
    return new_sentence               
    
def word_Latin(word):
    #converts words into pig Latin
    count=0
    for i in word:
        if word[0] in "aeiou":
            return word+"way"         
                 
        if i in "bcdfghjklmnpqrstvxyz":
            count+=1
            continue
        if i in "aeiou":
            count+=1
            return word[count-1:]+'a'+word[0:count-1]+'ay'   

def word_English(word):
    for i in word:
        if word[-3:]=="way":
            return word[:-3]
        
        elif word[-2:]=='ay':
            word=word[:-2]
            r_word=word[::-1]
            pos=r_word.find('a')
            first_word=r_word[:pos]
            first_word=first_word[::-1]
            last_word=r_word[pos+1:]
            last_word=last_word[::-1]
            final_word=first_word+last_word
            return final_word
