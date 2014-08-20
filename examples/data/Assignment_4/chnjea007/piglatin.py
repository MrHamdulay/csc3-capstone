# assignment 4 question 3
vowels = "aeiouAEIOU"
def toPigLatin(s):
    english = ""
    
    s = s.split()
    
    for i in s:
        index = len(i) + 1
        if i[0] in vowels:
            english += i + "way"
        else:
            for j in range(len(i)):
                if i[j] in vowels:
                    index = j
                    break
            english += i[index:] + "a" + i[:index] + "ay"
        english += " "
    return english
def toEnglish(s):
    pigLatin = ""
    index = 0
    s = s.split()
    for i in s:
        if i[-3] == "w":
            pigLatin += i[:-3]
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            pigLatin += i[index+1:-2] + i[:index]
        pigLatin += " "
    return pigLatin