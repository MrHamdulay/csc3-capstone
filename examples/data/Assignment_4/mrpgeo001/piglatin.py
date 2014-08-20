#Pig Latin Translator!!!
#Geoff Murphy 
#MRPGEO001
#2 April 2014

#Translate = input("(E)nglish or (P)ig Latin?\n")

#-------------------------------------------------------------------------------

def toPigLatin(s):
    sentence = ""
    for words in s.split():
        init = words[0] #Takes the first letter
        n = 0
        ay = "ay"
        if init in 'aeiou': #Checks if first letter is a vowel
            words += "way"
            sentence += (words + " ")
            continue
        else:
            words += "a"
            for i in words:
                if i in 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM': #If 1st letter is consonant, appends said letter and removes original copy
                    append = i
                    append = str(append)
                    words += append
                    words = words[1:]
                else:
                    break
        words += ay
        sentence += (words + " ")
    new_s = str(sentence)
    return new_s
    #print(sentence)
    
#--------------------------------------------------------------------------------
    
def toEnglish(s):
    sentence = ""
    for words in s.split():
        length_word = len(words)
        way = words[length_word:-4:-1] #Checks the back letters
        n = 0
        ay = "ay"
        if way == "yaw":
            words = words[0:-3] #prints without way
            sentence += (words + " ")
            continue
        elif way != "yaw":
            words = words[0:-2] #Removes ay
            backwards = words[::-1] #reverses order of letters
            for i in backwards:
                if i != 'a': #continues until an 'a' is reached
                    append = i
                    words = (append + words) #Adds letter to front of word
                    words = words[0:-1] #...and then removes that letter
                    continue
                elif i == 'a':
                    words = words[0:-1] #Removes the 'a' from "palindromising" 
                    break
        sentence += (words + " ")
    new_s = sentence
    return new_s
    #print(sentence)

#-------------------------------------------------------------------------------

#if Translate == "E":
    #s = input("Enter an English sentence:\n")
    #toPigLatin(s)
#elif Translate == "P":
    #s = input("Enter a Pig Latin sentence:\n")
    #toEnglish(s)
    
#-------------------------------------------------------------------------------