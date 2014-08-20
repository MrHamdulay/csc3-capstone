vowel_list = "aeiou"
def toPigLatin(s):
    word = ""
    s = s.split()
    for i in s:
        w_c = len(i) + 1
        if i[0] in vowel_list:
            word += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowel_list:
                    w_c = j
                    break
            word += i[w_c:] + "a" + i[:w_c] + "ay"
        word += " "
    return word
def toEnglish(s):
    word = ""
    w_c = 0
    s = s.split()
    for i in s:
        if i[-3] == "w":
            word += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    w_c = j
                    break
            word += i[w_c+1:-2] + i[:w_c]
        word += " "
    return word