vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def find_vowel(word):
    for i in range(len(word)):
        if word[i] in vowels:
            return i
    return -1

def toPigLatin(s):
    sentence = s.split(" ")
    piglatin = ""
    for word in sentence:
        vowel = find_vowel(word)
        if(vowel == -1):
            piglatin += ('a' + word + 'ay'+ ' ')
        elif(vowel == 0):
            piglatin += (word + "way" + ' ')        
        else:
            piglatin += (word[vowel:] + 'a' + word[:vowel] + "ay" +  ' ')
        
    return piglatin


def toEnglish(s):
    sentence = s.split(" ")
    english = ""
    for word in sentence:
        if word[:len(word) - 4:-1] == 'yaw':
            english += word[:len(word) - 3] + " "
        else:
            index = -3
            
            for letter in reversed(word[:-3]):
                if letter != 'a':
                    index-=1
                else:
                    break
            english +=  word[index:-2] + word[:index-1] + " "
    return english