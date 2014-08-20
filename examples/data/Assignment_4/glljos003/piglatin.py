vowels = "aeiou"
def toPigLatin(s):
    words = ""
    s = s.split()
    for i in s:
        index = len(i) + 1
        if i[0] in vowels:
            words += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowels:
                    index = j
                    break
            words += i[index:] + "a" + i[:index] + "ay"
        words += " "
    return words
def toEnglish(s):
    words = ""
    index = 0
    s = s.split()
    for i in s:
        if i[-3] == "w":
            words += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            words += i[index+1:-2] + i[:index]
        words += " "
    return words