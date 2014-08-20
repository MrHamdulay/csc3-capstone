#Write a module to translate sentences between English and a variant of Pig Latin (see: http://en.wikipedia.org/wiki/Pig_Latin).

#To convert from English to Pig Latin, each word must be transformed as follows:

#if the word begins with a vowel, "way" should be appended (example: apple becomes appleway)
#if the word begins with a sequence of consonants, this sequence should be moved to the end, prefixed with "a" and followed by "ay" (example: please becomes easeaplay)
#Assume that the English text does not contain the letter "w".


def toPigLatin(s):
    vowels = ("a","e","i","o","u")
    Word = ""
    NewWord = ""
    NewString = ""
    while s.find(' ')!=-1: # not found
        Word = s[0:s.index(" ")]
        if Word[:1] in vowels:
            NewWord = Word + "way"
            NewString = NewString + " " + NewWord 
        elif (Word[:1] not in vowels) and (Word[1:2] not in vowels) and (Word[2:3] not in vowels) and (Word[3:4] not in vowels): 
            NewWord = Word[4:] + "a" + Word[0:4] + "ay"   
            NewString = NewString + " " + NewWord
        elif (Word[:1] not in vowels) and (Word[1:2] not in vowels) and (Word[2:3] not in vowels):       
            NewWord = Word[3:] + "a" + Word[0:3] + "ay"
            NewString = NewString + " " + NewWord 
        elif (Word[:1] not in vowels) and (Word[1:2] not in vowels): 
            
            NewWord = Word[2:] + "a" + Word[0:2] + "ay"
            NewString = NewString + " " + NewWord
        elif  (Word[:1] not in vowels): 
            
            NewWord = Word[1:] + "a" + Word[0:1] + "ay"
            NewString = NewString + " " + NewWord
        else:
            NewString = NewString + " " + Word
        s = s.replace(Word + " ", "", 1)
        
        
    Word = s  
    if Word[:1] in vowels:
        NewWord = Word + "way"
        NewString = NewString + " " + NewWord
    elif (Word[:1] not in vowels) and (Word[1:2] not in vowels) and (Word[2:3] not in vowels) and (Word[3:4] not in vowels): 
        NewWord = Word[4:] + "a" + Word[0:4] + "ay"   
        NewString = NewString + " " + NewWord
    elif (Word[:1] not in vowels) and (Word[1:2] not in vowels) and (Word[2:3] not in vowels): 
        NewWord = Word[3:] + "a" + Word[0:3] + "ay"
        NewString = NewString + " " + NewWord
    elif (Word[:1] not in vowels) and (Word[1:2] not in vowels): 
        NewWord = Word[2:] + "a" + Word[0:2] + "ay"  
        NewString = NewString + " " + NewWord
    elif  (Word[:1] not in vowels): 
        NewWord = Word[1:] + "a" + Word[0:1] + "ay"
        NewString = NewString + " " + NewWord
    else:
        NewString = NewString + " " + Word     
    NewString = NewString[1:]
    return NewString


def toEnglish (s):
    Word = ""
    NewWord = ""
    NewString = "" 
    while s.find(' ')!=-1: # not found elloaHay orldaWay
        alpha = ""
        Word = s[0:s.index(" ")]  
        if Word[len(Word):len(Word) - 4:-1]  == "yaw":
            NewWord = Word[0:len(Word) - 3]
            NewString = NewString + NewWord + " "
        elif Word[len(Word):len(Word) - 3: -1] == "ya":
            NewWord = Word[:len(Word) - 2]
            lenWord = len(NewWord) 
            while NewWord[lenWord:lenWord - 1:-1] != "a":
                alpha = NewWord[lenWord:lenWord - 1:-1] + alpha
                lenWord = lenWord - 1
            NewString = NewString + alpha + NewWord[0:lenWord] + " "
        s = s.replace(Word + " ", "", 1)   
    
    #Last
    alpha = ""
    if s[len(s):len(s) - 4:-1]  == "yaw":
        NewWord = s[0:len(s) - 3]
        NewString = NewString + NewWord
    elif s[len(s):len(s) - 3: -1] == "ya" :
        NewWord = s[:len(s) - 2]
        lenWord = len(NewWord) 
        while NewWord[lenWord:lenWord - 1:-1] != "a" and lenWord > 0:
            alpha = NewWord[lenWord:lenWord - 1:-1] + alpha
        
            lenWord = lenWord - 1
        NewString = NewString + alpha + NewWord[0:lenWord] + " "    
    
    return NewString

toPigLatin("bbab bbba bbbb")