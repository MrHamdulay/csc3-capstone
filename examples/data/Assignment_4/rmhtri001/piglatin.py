def vowel_locator (word):

    vowels= ["a","e","i","o","u","A","E","I","O","U"]    
    x = len(word)
    for i in range(x): 
        if word[i] in vowels:
            return i
    return -1
def toPigLatin (s):

    words = s.split()
    vowels= ["a","e","i","o","u","A","E","I","O","U"]
    
    converted_sentence = ""
    for word in words:
        vowel = vowel_locator(word)
        if vowel == -1:
            converted_word= "a"+word+"ay"
            converted_sentence = converted_sentence + converted_word + " "
        elif vowel == 0 :
            converted_word= word+"way"
            converted_sentence = converted_sentence + converted_word + " "
        else:
            converted_word=word[vowel:]+"a"+word[:vowel]+"ay"
            converted_sentence = converted_sentence + converted_word + " "
    return converted_sentence

def toEnglish (s):
    
    words = s.split()
        
    converted_sentence = ""
    for word in words:
        if word[-3:] == "way":
            converted_word= word[:-3]
            converted_sentence = converted_sentence + converted_word + " "
        else:
            converted_word=word[:-2]
            splice = converted_word.rfind("a")
            converted_word  = converted_word[splice+1:]+converted_word[:splice]
            converted_sentence = converted_sentence + converted_word + " "
    return converted_sentence 
    