"""a module to translate sentences between English and a variant of Pig Latin
Author: Afika Nyati
Date: 1 April 2014"""

def toPigLatin(s):
    
    Vowels = ["a", "e", "i", "o", "u"]
    
    PigLatin = ""
    for word in s.split():
        if word[0] in Vowels:
            word += "way "
            PigLatin += word
        
        else:
            FirstConsonant = 50 #Random Number to initial FirstConsonant
            for nextvowel in range(5): # There are 5 vowels in the Vowels list
                y = word.find(Vowels[nextvowel])
                
                if FirstConsonant > y and y !=-1:
                    FirstConsonant = y
                        
            consonantsubstring = word[:FirstConsonant]
            remaindersubstring = word[FirstConsonant:]
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


if __name__ == "__main__":
    
    Choice = input("(E)nglish or (P)ig Latin?\n")
    
    Choice = Choice.lower()
    if Choice == "e":
        EngSent = input("Enter an English sentence:\n")
        print("Pig-Latin:\n", toPigLatin(EngSent), sep="")
    
    if Choice == "p":
        PigSent = input("Enter a Pig Latin sentence:\n")
        print("English:\n", toEnglish(PigSent), sep="")
        
            
            

    




    