def toPigLatin(s):
    
    vowels = ["a", "e", "i", "o", "u"]
    
    pig = ""
    for word in s.split():
        if word[0] in vowels:
            word += "way "
            pig += word
        
        else:
            oneconst = 100
            for nextvowel in range(5): 
                x = word.find(vowels[nextvowel])
                
                if oneconst > x and x !=-1:
                    oneconst = x
                        
            const = word[:oneconst]
            rem = word[oneconst:]
            word = rem + "a" + const + "ay "
            pig += word            
                
                
    pig = pig.rstrip()
    
    return pig


def toEnglish(s):
    
    eng = ""
    for word in s.split():
        x = len(word)
        
        if word[x - 3:x] == "way":
            word = word[0:x-3]
            eng += word + " "
            
        else:
        
            a_fix = word[:x-2].rfind("a")
    
            end = word[0:a_fix]
            start = word[a_fix+1:x-2]
            word = start + end
            eng += word + " "
            
    eng = eng.rstrip()
    
    return eng


if __name__ == "__main__":
    
    Choice = input("(E)nglish or (P)ig Latin?\n")
    
    Choice = Choice
    if Choice == "e":
        EngSent = input("Enter an English sentence:\n")
        print("Pig-Latin:\n", toPigLatin(EngSent), sep="")
    
    if Choice == "p":
        PigSent = input("Enter a Pig Latin sentence:\n")
        print("English:\n", toEnglish(PigSent), sep="")
        
            
            

    




    