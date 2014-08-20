# A program to translate English and Pig latin
# Alison Hoernle
# HRNALI002
# 1 April 2014

def toPigLatin(s):
    # make all letters in lowercase
    pig_latin = ''
    
    # to split all the words of the sentence so that each word is changed
    for i in s.split(' '):
    
        # check if first letter is a vowel
        if i[0] in 'aeiouAEIOU':
            word = i + 'way'
        
        # if first letter is a consonant
        else:
            cons_group = '' #consonant group starts as the first letter which we know is a consonant
            for l in range(0, len(i)):
                letter = i[l]
                if letter in 'aeiouAEIOU': #if the letter is a consonant then the loop must break
                    break
                else:
                    cons_group = cons_group + letter # The consonant group should be all the first letters until a vowel was reached
                    l += 1
                    rest_of_word = i[l:len(i)+1] # The rest of the word should be from the letter after the consonant group to the end
                    word = rest_of_word + 'a' + cons_group + 'ay'
        pig_latin = pig_latin + ' ' + word  # Formula for pig latin
    pig_latin = pig_latin[1:]
    return pig_latin

def toEnglish(s):
    # make all letters in lower case
    
    english = ''
    
    #split each word of the sentence
    for i in s.split():
    
        # if word ends in way, then s is the word without the 'way'
        if i[-1:-4:-1] == 'yaw':
            word = i[0:-3:1]
        
        
        # for the consonant group of piglatin words that end in ay
        else:
            cons_group = ''
            cons_group_rev = ''
            for l in range(0, len(i)-2):
                letter = i[-3-l] # goes from the back and checks each letter up until it reaches an a...
                if letter == 'a':
                    break
                
                else:
                    cons_group_rev = cons_group_rev + letter
                    l += 1
                
                    cons_group = cons_group_rev[::-1] # making the consonants show in the right order
                
                    # For the rest of the word
                    x = len(cons_group) + 3 #the vowels are going to be up until the consonants plus the 'a' at beginning and the 'ay' at end
                rem_word = i[0:len(i)-x]
                word = cons_group + rem_word
            
            # final formula for the whole word
        english = english + ' ' + word
    english = english[1:]
    return english      
        
                    
            
            
        