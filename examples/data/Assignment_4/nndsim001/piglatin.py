# Thismodulepiglatin.pycontain functions that convert from English to Pig Latin
# using the following rules

# If the word begins with a vowel, "way" should be appended 
# (example: apple becomes appleway)
# If the word begins with a sequence of consonants, this sequence should be 
# moved to the end, prefixed with "a" and followed by "ay" 
# (example: please becomes easeaplay)

# It is also assumed that the English text does not contain the letter "w".

# toPigLatin (s), to return the Pig Latin string for a given English string
# toEnglish (s), to return the English string for a given Pig Latin string

# Student Name: Simeon Nandjembo

# Student Number: NNDSIM001

# 04 April 2014

# This function return the Pig Latin string for a given English string
def toPigLatin(s):    
    splitted = str(s).split(" ")
    vowels = ("aeiou")
    
    handle = ""
    hand = ""  
    
    
    # This loop access a string in the array one at a time and passes it to the 
    # inside loop for manipulation
    for i in range(len(splitted)):
        handle = splitted[i]
        
        # Checks if the first character is a vowel
        if handle[0] in vowels:
            hand += handle + "way "
            handle = ""
            continue
        elif len(handle) == 1:
            hand += "a" + handle + "ay "
            handle = ""
            continue
        else:
            # Inside loop that looks for the next vowel in the string
                    
            while True:
                pos = 0
                vowel = ""            
                # This loops finds the position of all vowels in the string
                for j in handle:
                    pos += 1
                    if j in vowels:
                        vowel += str(pos)
                
                # Testing to see if any vowel positions was recorded        
                # If not, the else statement is executed
                if vowel != "":
                    hand += handle[int(vowel[0])-1:] + "a" + handle[:int(vowel[0])-1] + "ay "
                    handle = ""
                    pos = 0
                    vowel = []                     
                    break
                else:
                    hand += "a" + handle + "ay "
                    handle = ""
                    pos = 0
                    vowel = []                       
                    break
                           
    return hand[:len(hand)-1]



# This function return the English string for a given Pig Latin string
def toEnglish(s):
    splitted = str(s).split(" ")
    handle = ""
    hand = ""   
    
    # This loop access a string in the array one at a time and passes it to the 
    # inside loop for manipulation
    for i in range(len(splitted)):
            handle = splitted[i] 
            
            # look for "way" at the end of the string
            if handle[len(handle)-3] == "w":
                # Check if the last chacter is "y"
                if handle[len(handle)-1] == "y":
                    # Confirm if "a" is in the middle of "w" and "y"
                    if handle[len(handle)-2] == "a":
                        # At this point, it is confirmed that "way" is at the end
                        hand += handle[:len(handle)-3] + " "
                        handle = ""
                        continue
            else:
                # At this point, it is know that "way" not at the end
                # Next step is to find the next "a" in the string
                for j in range(1,len(handle)):
                    if handle[j] == "a":
                        # Its already known that "ay" is at the end if not "way"
                        hand += handle[j+1:len(handle)-2] + handle[:j] + " "
                        handle = ""
                        break
                                      
    return hand[:len(hand)-1]



#Sample I/O:

# (E)nglish or (P)ig Latin?
# E
# Enter an English sentence:
# the quick black fox jumps over the lazy apple
# Pig-Latin:
# eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway

# Sample I/O:

# (E)nglish or (P)ig Latin?
# P
# Enter a Pig Latin sentence:
# eathay uickaqay ackablay oxafay umpsajay overway eathay azyalay appleway
# English:
# the quick black fox jumps over the lazy apple