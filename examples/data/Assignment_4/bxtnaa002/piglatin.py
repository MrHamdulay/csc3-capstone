def toPigLatin(s):
    eng = s.split()
    x = ""
    for i in eng:
        if i[0] in "AEIOUaeiou":
            x += i+"way"+" "
        elif i[0] not in "AEIOUaeiou":
            d = -1
            for k in i:
                if k not in "AEIOUaeiou":
                    d += 1
                if k in "AEIOUaeiou": break
            x += i[d+1:len(s)+1]+"a"+i[0:d+1]+"ay"+" "
    return x

def toEnglish(s):
    pig = s.split()
    x = ""
    for i in pig:
        if "way" in i:
            x += i[0:i.find("way")]+" "
        elif i.count("a")==2:
            adds = i[i.find("a")+1:i.find("ay")]
            x += adds+i[0:i.find("a")]+" "
        elif i.count("a")>=2:
            i = i[0:len(i)-2]
            d = i[i.rfind("a")+1:len(i)]
            x += d+i[0:i.rfind("a")]+" "
    return x