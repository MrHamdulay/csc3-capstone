def toPigLatin (s):
    start = 0
    new_s = ""
    for word in s.split(" "):
        consonants = ""
        i = 0
        newword = ""
        if word[0] == "A" or word[0] == "a" or word[0] == "E" or word[0] == "e" or word[0] == "I" or word[0] == "i" or word[0] == "O" or word[0] == "o" or word[0] == "U" or word[0] == "u":
            newword = word + "way"
        else:
            for char in word:
                if char == "A" or char == "a" or char == "E" or char == "e" or char == "I" or char == "i" or char == "O" or char == "o" or char == "U" or char == "u":
                    newword = word[i::1] + "a" + consonants + "ay"
                    break
                else:
                    consonants += char
                    i += 1
            else: #no vowels in word
                newword = "a" + consonants + "ay"
        new_s += " " + newword
    return new_s[1::]
 
def toEnglish (s):
    start = 0
    new_s = ""
    for word in s.split(" "):
        consonants = ""
        i = 0
        length = len(word)
        newword = ""
        if word[length - 3::1] == "way":
            newword = word[0:length - 3:1]
        else:
            for char in word[length - 3::-1]:
                if char != "A" and char != "a" and char != "E" and char != "e" and char != "I" and char != "i" and char != "O" and char != "o" and char != "U" and char != "u":
                    consonants += char
                    i += 1
                else:
                    newword = consonants[::-1] + word[0:length - i - 3:1]
                    break
        new_s += " " + newword
    return new_s[1::]   