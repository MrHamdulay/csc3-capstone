def toPigLatin(s):
    x = s.split()
    phrase = ""
    for i in x:
        if i[0] in "aeiouAEIOU":
            phrase += i+"way"+" "
        elif i[0] not in "aeiouAEIOU":
            c = -1
            for j in i:
                if j not in "aeiouAEIOU":
                    c += 1
                if j in "aeiouAEIOU": break
            phrase += i[c+1:len(s)+1]+"a"+i[0:c+1]+"ay"+" "
    return phrase

def toEnglish(s):
    xx = s.split()
    part = ""
    for y in xx:
        if "way" in y:
            part += y[0:y.find("way")]+" "
        elif y.count("a")==2:
            cons = y[y.find("a")+1:y.find("ay")]
            part += cons+y[0:y.find("a")]+" "
        elif y.count("a")>=2:
            y = y[0:len(y)-2]
            c = y[y.rfind("a")+1:len(y)]
            part += c+y[0:y.rfind("a")]+" "
    return part 