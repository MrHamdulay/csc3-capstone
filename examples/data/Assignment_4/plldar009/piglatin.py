vowelstring = "aeiou"
def toPigLatin(s):
    text = ""
    s = s.split()
    for i in s:
        index = len(i) + 1
        if i[0] in vowelstring:
            text += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowelstring:
                    index = j
                    break
            text += i[index:] + "a" + i[:index] + "ay"
        text += " "
    return text
def toEnglish(s):
    text = ""
    index = 0
    s = s.split()
    for i in s:
        if i[-3] == "w":
            text += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            text += i[index+1:-2] + i[:index]
        text += " "
    return text