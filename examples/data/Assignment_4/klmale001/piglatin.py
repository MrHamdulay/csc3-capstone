vowels = ('AEIOUaeiou')

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
            noay = word[:len(word) - 2]
            firstconsonants = noay.split("a")[-1]
            consonantsremoved = noay[:len(noay) - (len(firstconsonants)+1)]
            english += firstconsonants + consonantsremoved + " "
    return english