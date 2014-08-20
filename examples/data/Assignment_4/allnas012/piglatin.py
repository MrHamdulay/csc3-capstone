def find_vowel(word):
    # This is from 0 to the length of the word
    for i in range(len(word)):
        if word[i] in vowel:
            return i
    # Return an error value if there are not any (which solves another problem too!)
    return -1
vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")

def toPigLatin(s):
    x = s.split(" ")
    y = ("")
    for word in x:
        if word[0] in vowel:
            y += (word + "way" + " ")
        else:
            findvowel = 0
            for letter in word:
                if letter not in vowel: 
                    findvowel += 1
                    continue
                else: 
                    break
            y += (word[findvowel:] + "a" + word[:findvowel] + "ay" +" ") 
    return y[:len(y) - 1]

def toEnglish(s):
    x = s.split(" ")
    e = ("")
    for word in x:
        if word[:len(word) - 4:-1] == 'yaw':
            e += (word[:len(word) - 3] + " ")
        else: 
            noay = word[:len(word) - 2]
            fc = noay.split("a")[-1]
            cr = noay[:len(noay) - (len(fc)+1)]
            e += (fc + cr + " ")
    return (e)