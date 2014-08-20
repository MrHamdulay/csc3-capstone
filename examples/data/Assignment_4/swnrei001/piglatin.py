# A module to convert to and from Pig Latin
# 31-03-2014
# Author: SWNREI001

vowels = "aeiou"
def toPigLatin_word(s):
    begin = ""
    ans = ""
    for i in s:
        if not (i.lower() in vowels):
            begin += i
        else:
            break
    if len(begin) > 0:
        ans = s[len(begin):] + "a" + begin + "ay"
    else:
        ans = s + "way"
    return ans

def toEnglish_word(s):
    if s.endswith("way"):
        return s[:len(s)-3]
    else:
        s = s[:len(s) - 2]
        begin = ""
        count = 0
        for i in s[::-1]:
            if (not i.lower() in vowels):
                begin = i + begin
                count = count + 1
            else: break
        return begin + s[:len(s) - len(begin) - 1] #-1 to remove trailing a

def toPigLatin(s):
    strings = s.split(" ")
    ans = ""
    for i in strings:
        if i == "":
            continue
        ans = ans + toPigLatin_word(i) + " "
    return ans

def toEnglish(s):
    strings = s.split(" ")
    ans = ""
    for i in strings:
        if i == "":
            continue
        ans = ans + toEnglish_word(i) + " "
    return ans