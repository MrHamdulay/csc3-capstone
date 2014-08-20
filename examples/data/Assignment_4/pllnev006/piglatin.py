# Module containing functions for Pig Latin translations
# Nevarr Pillay - PLLNEV006
# 30 March 2014

vowels = ["a","e","i","o","u"]

def toPigLatin(input):
    words = input.split()
    newstring = ""
    for word in words:
        word.lower()
        check = False
        for vowel in vowels:
            if word[:1] == vowel:
                newstring += word + "way "
                check = True
                break
        if check == True: continue    
        index = 0    
        for letter in range(len(word)):
            if index > 0: break
            for vowel in vowels:
                if word[letter] == vowel:
                    index = letter
                    break
        if index == 0: index = len(word)        
        newstring += word[index:] + "a" + word[:index] + "ay "
    return newstring               

def toEnglish(input):
    words = input.split()
    newstring = ""
    for word in words:
        word.lower()
        if word[len(word)-3:] == "way":
            newstring += word[:len(word)-3] + " "
            continue
        index = len(word)
        for i in range(len(word)-3,-1,-1):
            if "a" == word[i]:
                index = i
                break
        newstring += word[index+1:len(word)-2] + word[:index] + " "
    return newstring       


    

    