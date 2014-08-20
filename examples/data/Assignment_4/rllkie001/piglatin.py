# Kieran Reilly, RLLKIE001
# PigLatin Translater
# 01/04/14

def toPigLatin(s):
    english = s.lower()
    pigLatin = ""
    convertWord = ""
    convertedWord = ""
    words = english.split(" ")
    vowels = ['a','e','i','o','u']
    a = "a"
    e = "e"
    i = "i"
    o = "o"
    u = "u"
    
    
    for i in range(len(words)):     #first loop to store a new word
        convertWord = words[i]
        for j in range(len(convertWord)):  #third loop to vowls in vowels
            if convertWord[0] == a or \
               convertWord[0] == e or \
               convertWord[0] == i or \
               convertWord[0] == o or \
               convertWord[0] == u :
                convertedWord = convertWord + "way"
                words[i] = convertedWord
                break
        
        else:
            sub = ""
            count = 0
            for k in range(len(convertWord)):
                if(convertWord[k] != a and \
                   convertWord[k] != e and \
                   convertWord[k] != i and \
                   convertWord[k] != o and \
                   convertWord[k] != u ):
                    sub = sub + convertWord[k]
                    count = k+1
                
                elif(convertWord[k] == a or \
                     convertWord[k] == e or \
                     convertWord[k] == i or \
                     convertWord[k] == o or \
                     convertWord[k] == u ):
                    break
            convertedWord = convertWord[count:] + "a" + sub + "ay"
            words[i] = convertedWord
        print(words[i]+" ",end= '')
       # pigLatin = pigLatin + " " + words[i] + " "                
    
    
    #print(pigLatin[1:], end='')
    
    
    
def toEnglish(s):
    
    piglatin = s.lower()
    words = piglatin.split(" ")
    english = ""
    
    for i in range(len(words)):
        convertWord = words[i]
        
        length = len(convertWord)
        if convertWord[length - 3] == "w":
            convertedWord = convertWord[:length-3]
            words[i] = convertedWord
            
        elif convertWord[length - 3] != "w":
            sub = convertWord[:length-2]
            for j in range(len(sub)):
                if sub[-1-j] == "a":
                    semiConvert = sub[:-1-j] + "" + sub[-j:]
                    count = j
                    break
            
            semiConvertLength = len(semiConvert)
            convertedWord = semiConvert[-count:] + semiConvert[:semiConvertLength-count]
            words[i] = convertedWord
        english = english + " " + words[i] + " "
        print(words[i]+" ", end='')
    #print(english[1:], end='')
    
if __name__ == "__main__":
    choice = input("(E)nglish or (P)ig Latin? \n")
    
    if choice == "E":
        s = input("Enter an English sentence: \n")
        print("Pig-Latin: \n")    
        
        toPigLatin(s)
        
    
    elif choice == "P":
        s = input("Enter a Pig Latin sentence: \n")
        print("English:  \n")
        
        toEnglish(s)
        
    