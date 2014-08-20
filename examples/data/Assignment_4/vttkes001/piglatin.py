import math

def noVowel(b):
    Wordsplit = list(b)
    countletter = len(Wordsplit)
    counter = 0
    check = 0
    for m in range(countletter):
        if Wordsplit[counter] in ("a","e","i","o","u"):
            check = 1
        counter = counter + 1
    if check == 1:
        empty = ""
        return empty
    
    if check == 0:
        word = ("a" + b + "ay ")
        return word


def toPigLatin(s):
    splitArr = s.split(" ")
    count = s.count(" ")
    count = count + 1
    
    loopcounter = 0
    NewSentence = ""
    for i in range(count):
        wordsplit = list(splitArr[loopcounter])
        countword = len(wordsplit)
        
        Novowels = noVowel(splitArr[loopcounter])
        NewSentence = NewSentence + Novowels 
    
        
        if wordsplit[0] in ("a","e", "i", "u", "o"):
            NewWord = (splitArr[loopcounter] +"way ")
            NewSentence = NewSentence + NewWord 
        else:
            counter2 = 0
            for j in range(countword):
                if wordsplit[counter2] in ("a", "e", "i", "u", "o"):
                    newWord = (splitArr[loopcounter])[0:counter2]
                    KingWord = ((splitArr[loopcounter])[counter2:] + "a" + newWord + "ay ")
                    NewSentence = NewSentence + KingWord 
                    break
                counter2 = counter2 + 1
        loopcounter = loopcounter + 1
        
    return NewSentence
    
def toEnglish(s):
    
    splitArr = s.split(" ")

    count = s.count(" ")

    
    
    loopcounter = 0
    NewSentence = ""
    for i in range(-1,count):
        wordsplit = list(splitArr[loopcounter])
        countword = len(wordsplit)   
        
        if((splitArr[loopcounter])[countword - 3:] == "way"):
            NewWord = (splitArr[loopcounter])[0: countword - 3]
            NewSentence = NewSentence + NewWord + " "
        else:
            
            if((splitArr[loopcounter])[countword - 2:] == "ay"):
                LoseAY = (splitArr[loopcounter])[0: countword - 2]
                PositionA = LoseAY.rfind("a")
                EndConsonants = LoseAY[PositionA + 1: countword - 2]
                StartWord = LoseAY[0 : PositionA]
                EnglishWord = EndConsonants + StartWord
                NewSentence = NewSentence + EnglishWord + " " 
        loopcounter = loopcounter + 1
    return NewSentence
