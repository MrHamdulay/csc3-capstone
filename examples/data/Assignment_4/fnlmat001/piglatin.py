# Matthew Finlayson - FNLMAT001
# 29/03/14
# Assignment 4 - Question 2
# piglatin.py


def toPigLatin(english):
    #english = english.lower()
    english = english.split(" ")
    #print(english)
    pigLatin = ""
    
    for i in (english): #loops through each word in the string supplied
        
        if (i[0] in "aeiou"): # if the first letter of the word is a vowel
            newWord = i+"way" # add 'way' onto the word
            pigLatin += newWord # add the new word onto the string of pigLatin            
        else: # the first letter of the word is not a vowel
            sequence = "" #variable to keep track of the string of consonants before the first vowel is reached
            for j in i: #loops through the characters in each word
                if j not in "aeiou": # if the character is a consonant
                    sequence = sequence+j # add the consonant onto the sequence
                else: # if the character is a vowel
                    break # then the loop exits because no further processing for the word is needed
            newWord = i[len(sequence):]+"a"+sequence # the word - i - is sliced to cut off the sequence of consonants at the front, and the sequence of consonants is added to the sliced word
            pigLatin += newWord+"ay" # ay is added finally after the consonants have been moved            
        pigLatin+=" " # adds a space after each word is created
        
    pigLatin=pigLatin[:-1] # ensures there isn't a space after the pigLatin string
    
    return pigLatin

def toEnglish(pigLatin):
    #pigLatin = pigLatin.lower()
    pigLatin = pigLatin.split(" ")    
    #print(pigLatin)
    english = ""
    
    for i in (pigLatin): # loops through each word
        if (i[len(i)-3:] == "way"): # if the word started with a vowel initially
            english+=i[:len(i)-3] # slice the word to exclude 'way' that was added
            
        else: # otherwise, the word didn't start with a vowel
            position = 0 # variable used to keep track of the position of the characters
            sequence = "" # variable to store the sequence of consonants that was moved to the end
            newWord = i[:len(i)-2] # slices the word - i - to exclude 'ay' that was added            
            for j in i: # loops through each character of the word
                if newWord[len(newWord)-position-1] not in "aeiou": #if the letter is a consonant / the code reads the word - newWord - from back to front
                    #print (newWord[len(newWord)-position-1]) 
                    sequence = newWord[len(newWord)-position-1]+sequence # adds the consonant onto the sequence of consonants to be moved
                    position+=1
                elif newWord[len(newWord)-position-1] == "a": # if the next letter is not a consonant and is 'a'
                    newWord = sequence + newWord[:len(newWord)-len(sequence)-1] # the sequence is added to the front of the word and the 'a' at the end and the sequence of consonants is removed
                    break
            english+=newWord 
            
        english+=" "
    english = english[:-1]
    return english