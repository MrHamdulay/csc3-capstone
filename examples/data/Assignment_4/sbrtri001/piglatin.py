vowels = "aeiou"

def toPigLatin(a):
    string = ""
    a = a.split()
    for i in a:
        index = len(i) + 1
        if i[0] in vowels:
            string += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowels:
                    index = j
                    break
            string += i[index:] + "a" + i[:index] + "ay"
        string += " "
    return string

def toEnglish(a):
    string = ""
    index = 0
    a = a.split()
    for i in a:
        if i[-3] == "w":
            string += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            string += i[index+1:-2] + i[:index]
        string += " "
    return string