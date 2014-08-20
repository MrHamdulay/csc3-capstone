#program to convert sentence to PigLatin and vice versa
#Anthony Jacob
#2-4-14


def toPigLatin(s):
    
    Vowels = ["a", "e", "i", "o", "u"]
    
    PigLatin = ""
    for word in s.split():
        if word[0] in Vowels:
            word += "way "
            PigLatin += word
        
        else:
            First_Consonant = 50 #Random Number to initial FirstConsonant
            for next_vowel in range(5): # There are 5 vowels in the Vowels list
                y = word.find(Vowels[next_vowel])
                
                if First_Consonant > y and y !=-1:
                    First_Consonant = y
                        
            consonantsubstring = word[:First_Consonant]
            remaindersubstring = word[First_Consonant:]
            word = remaindersubstring + "a" + consonantsubstring + "ay "
            PigLatin += word            
                
                
    PigLatin = PigLatin.rstrip()
    
    return PigLatin


def toEnglish(s):
    
    English = ""
    for word in s.split():
        length = len(word)
        
        if word[length - 3:length] == "way":
            word = word[0:length-3]
            English += word + " "
            
        else:
        
            a_position = word[:length-2].rfind("a")
    
            end = word[0:a_position]
            start = word[a_position+1:length-2]
            word = start + end
            English += word + " "
            
    English = English.rstrip()
    
    return English



