#pig latin/english translator
#nicole henning
#due: 04/04/14
        
def toPigLatin (s):
    
    #translate whole sentence to pig latin - split, translate each word
    sentence = s.split(" ")
    translated = ""
    vowels = ("aeiou")
    for word in sentence:
        if word[0] in vowels:
            translated += word + "way" + " "
        else:
            position = 0
            for letter in word:
                if letter not in vowels: 
                    position += 1
                    continue
                else: 
                        break
            translated += word[position:] + "a" + word[:position] + "ay" + " "
    return translated[:len(translated) - 1]


def toEnglish (s):
    vowels = ("aeiou")
    #change to lower case?
    sentence = s.split(" ")
    translated = ""
    
    for word in sentence:
        #if word starts with a vowel and ends in "way", take away way
       
        if (word [0] in vowels) and (word [-3:] == "way"):
            translated += word[:-3]+ " "
            
        #else if sequence of consonents ends with ay and preceded by a
        else:
            word = word[0:len(word)-2]
            while word[-1] != 'a':
                word = word[-1] + word[0:len(word)-1]
            word = word[0:len(word)-1]
            translated +=word + " "            
                       
  
    return translated[:len(translated) - 1]
