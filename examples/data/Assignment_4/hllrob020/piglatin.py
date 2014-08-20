#Robin Hall
#Program to convert between pig latin and english
#4/4/2014

vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def toPigLatin(s):
    
    sentence = s.split(" ")
    latin = ""
    
    for word in sentence:
        if word[0] in vowels:
            latin += word + "way" + " "
        else:
            vowel_index = 0
            for letter in word:
                if letter not in vowels: 
                    vowel_index += 1
                    continue
                else: 
                    break
            
            latin += word[vowel_index:] + "a" + word[:vowel_index] + "ay" + " "
    
    return latin[:len(latin) - 1]

def toEnglish(s):
    
    sentence = s.split(" ")
    english = ""
    
    for word in sentence:
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " "
        else: 
            nosuffix = word[:len(word) - 2]
            prefix = nosuffix.split("a")[-1]
            consonants = nosuffix[:len(nosuffix) - (len(prefix)+1)]
            english += prefix + consonants + " "
            
    return english[:len(english) - 1]
    