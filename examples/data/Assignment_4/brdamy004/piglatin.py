# Assignment 4 question 3
# Amy Brodie
# 2/04/2014

def toPigLatin(s):
    s += " "
    new_s = ""
    for i in range(s.count(" ")):
        n = s.find(" ")
        word = s[:n]
        s = s[n+1:]
        if word[0].upper() in ["A","E","I","O","U"]:
            word += "way"
            new_s += word + " "
        else:
            for i in range(len(word)):
                if word[i] in ["a","e","i","o","u"]:
                    r = i
                    break
                else:
                    r=len(word)
            back = word[:r]
            word = word[r:] + "a" + back + "ay"
            new_s += word + " "
    return new_s[:-1]

def toEnglish(s):
    s += " "
    new_s = ""
    for i in range(s.count(" ")):
        n = s.find(" ")
        word = s[:n]
        s = s[n+1:]        
        if word[-3:] == "way":
            word = word[:-3]
            new_s += word + " "
        else:
            word = word[:-2]
            r = word[::-1].find("a") 
            word = word[-r:] + word[:-r-1]
            new_s += word + " "
    return new_s[:-1]