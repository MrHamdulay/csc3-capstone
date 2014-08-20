#mahdimarcus.
#mrcmahoo1
vowelstring = "aeiou"
def toPigLatin(s):
    w_string = ""
    s = s.split()
    for i in s:
        index = len(i) + 1
        if i[0] in vowelstring:
            w_string += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowelstring:
                    index = j
                    break
            w_string += i[index:] + "a" + i[:index] + "ay"
        w_string += " "
    return w_string
def toEnglish(s):
    w_string = ""
    index = 0
    s = s.split()
    for i in s:
        if i[-3] == "w":
            w_string += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            w_string += i[index+1:-2] + i[:index]
        w_string += " "
    return w_string