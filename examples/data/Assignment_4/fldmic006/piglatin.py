#create function to seperate string into individual words
def toPigLatin(string):
    #check for case where they only enter one letter
    if len(string) == 1:
        piglatin = toPig(string)
        
        return piglatin
        
    else:
        word = string.split()
        piglatin = ""
        
        for i in range(len(word)):
            pigLatin = toPig(word[i])
            piglatin += pigLatin + " "
        
        return piglatin

def toPig(word):
    upper = word.upper()
    pigLatin = ""
    vowel = 'A', 'E', 'I', 'O', 'U'
    
    #get first letter of word
    first = upper[0:1]
    
    #check if first is a vowel
    if(first in vowel):
        pigLatin = word + "way"
    
    #check for consonant of single letter
    elif(first != vowel and len(word) == 1):
        pigLatin = 'a' + word + "ay"
        
    else:
        i = 0
        sequence = ""  
        end = 1
        
        while end !=0:
            letter = word[(i-1):i]
            
            if(letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U' or letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' ):
                end = 0 #end the loop as a vowel has been reached
            elif(i > len(word)):
                end = 0#end the loop if string is all consonants
            
            else:
                sequence += letter #the sequence is what will be moved to the end of the string
                i += 1
                
        #compensate for extra addition to i
        i -= 1 #i is now the amount of consonants moved to the end of the original string
        
        #creat new string
        pigLatin = word[i:] + 'a' + sequence + "ay"
            
    return pigLatin

def toEnglish(string):
    #check if string is just one letter
    if( len(string) == 1):
        english = toEng(string)
        
        return english
        
    else:
        word = string.split()
        english = ""
    
        for i in range(len(word)):
            pigLatin = toEng(word[i])
            english += pigLatin + " "
    
        return english
    
def toEng(word):
    english = ""
    #check if word starts with a vowel and remove 'way'
    if(word[(len(word)-3):(len(word))] == "way"):
        english += word[:(len(word)-3)]

    #for single letter consonants
    elif(len(word) == 4):
        english = word[1]
    
    #check if last 2 letters are 'ay''
    elif(word[(len(word)-2):(len(word))] == "ay"):
        
        #remove all consonants which come before the 'a'
        con = ""
        letter = ''
        j = len(word)-2
        
        while letter != 'a':
            letter = word[j-1:j]
            
            if letter != 'a':
                con += letter
            j -= 1
        
        #reverse con because it is the consonants but backwards
        con = con[::-1]
        
        english = con + word[0:j]
    
           
        
    return english