vowelstring = "aeiou"
def toPigLatin(s):
    word = ""
    s = s.split()
    for i in s:
        index = len(i) + 1
        if i[0] in vowelstring:
            word += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowelstring:
                    index = j
                    break
            word += i[index:] + "a" + i[:index] + "ay"
        word += " "
    return word
def toEnglish(s):
    word = ""
    index = 0
    s = s.split()
    for i in s:
        if i[-3] == "w":
            word += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            word += i[index+1:-2] + i[:index]
        word += " "
    return word