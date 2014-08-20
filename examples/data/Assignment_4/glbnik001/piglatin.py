vowel = 'aeiou'
def toPigLatin(a):
    sentence =""
    a =a.split()
    for i in a:
        finder = len(i) +1
        if i[0] in vowel:
            sentence += i + "way"
        else:
            for h in range (len(i)):
                if i[h] in vowel:
                    index = h
                    break
            sentence += i[finder:] + "a" + i[:finder] + "ay"
        sentence += " "
    return sentence

def toEnglish(s):
    Translator = ""
    tracker = 0
    s = s.split()
    for t in s:
        if t[-3] == "w":
            Translator +=t[:-3]
        else:
            for p in range(len(t) - 3, -1, -1):
                if t[p] == "a":
                    tracker = p
                    break
            Translator += t[tracker+1:-2] + t[:tracker]
        Translator += " "
    return Translator
    

                

                

            
        

