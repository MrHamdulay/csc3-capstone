def toPigLatin(s):
    
    VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    
    words=s.split()
    
    for word in words:
        for i in word:
            if word[0] in VOWELS:
                return word +"ay"
            else: 
                return word[1:] + word[0] + "ay"
            
    
    

    
    