def toPigLatin (s):
    ans = ""
    first = True
    while len(s) != 0:
        if s.find(" ")!=-1:
            word = s[0:s.index(" ")]
            s = s[s.index(" ")+1:]
        else:
            word = s        
            s=""
        if "aeiou".find(word[0:1])!=-1:
            word += "way"
        else:
            countofcons = 1
            while "aeiou".find(word [countofcons:countofcons+1])==-1:
                countofcons+=1
            word = word[countofcons:] + "a" + word[0:countofcons] + "ay"
        if first:
            ans += word
        else:
            ans += " " + word
        first = False
    return ans
def toEnglish (s):
    ans = ""
    first = True
    while len(s) != 0:
        if s.find(" ")!=-1:
            word = s[0:s.index(" ")]
            s = s[s.index(" ")+1:]
        else:
            word = s        
            s=""
        if word[-3:] =="way":
            word = word[0:-3]
        else:
            word = word[-(4+(word[-4:: -1].find("a")))+1:-2] +(word[:-(4+(word[-4:: -1].find("a")))])
        if first:
            ans += word
        else:
            ans += " " + word
        first = False
    return ans