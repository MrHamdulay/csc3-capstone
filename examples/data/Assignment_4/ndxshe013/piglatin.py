def toPigLatin(s):
    words = s.split()
    vowels ="aeiou"
    for i in range(len(words)):
        if words[i][0] in vowels:
            words[i] = words[i]+"way"
        else:
            pos = 0
            for j in range(len(words[i])):
                if words[i][j] in vowels:
                    break
                else:
                    pos = pos +1
            words[i] = words[i][pos:] + "a" + words[i][:pos] + "ay"
                
    return " ".join(words)
def toEnglish(s):
    words = s.split()
    vowels ="aeiou"
    for i in range(len(words)):
        if words[i][-3:] == "way":
            words[i] = words[i][:-3]
        else:
            s = words[i][:-2]
            t  = s[s.rfind("a")+1:]
            s = s[:s.rfind("a")]
            s = t+s
            words[i] = s
            
    return " ".join(words)
#print(toEnglish("easeaplay"))