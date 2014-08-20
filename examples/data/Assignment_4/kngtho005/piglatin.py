# piglatin.py
# module to translate sentences between English and Pig Latin
#   def toPigLatin (s)
#     to return the Pig Latin string for a given English string
#   toEnglish (s)
#     to return the English string for a given Pig Latin string
# Thomas Konigkramer
# 29 March 2014

def toPigLatin(s):
    text = s.split(" ")
    x = s.count(" ") + 1 # s.count counts the number of gaps, thus 
                         # number of words is no. of gaps + 1.   
    piglatin = ""
                         
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVWXYZ" # w excluded because
                                                             # of -way suffix    
    for i in range(0,x):
        word = text[i] + " " # so that can be read as space and no letter
        if word[0] in vowels:
            piglatin += word[:-1] + "way" + " "
            
        elif word[0] in consonants:
            c = 0
            r = 1
            while word[c] in consonants:
                    newtext = word[r:-1] # to exclude space at end of word
                    cons = word[:r]
                    r += 1
                    c += 1
                    
            piglatin += newtext + "a" + cons + "ay" + " "
    
    return piglatin

def toEnglish(s):
    text = s.split(" ")
    x = s.count(" ") + 1 # s.count counts the number of gaps, thus 
                             # number of words is no. of gaps + 1.   
    english = ""
                             
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVWXYZ" # w excluded because
                                                            # of -way suffix    
    for i in range(0,x):
        word = text[i] + " "
        if word[-4:] == "way ":
            english += word[0:-4] + " "
            
        elif word[0] in vowels:
            word = word[:-3]  # to exlude the ay suffix
            r = len(word) - 1
            cons = ""
            while word[r] in consonants:
                    cons += word[r]
                    newword = word[:r]
                    r -= 1
                    
            english += cons[::-1] + newword[:-1] + " " # newword[:-1] to exclude a
                                                       # cons[::-1] because were 
                                                       # wrong way around   
    
    return english