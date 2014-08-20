def toPigLatin(s):
    p = s.split()
    y = ""
    for i in p:
        if i[0] in "AEIOUaeiou":
            y += i+"way"+" "
        elif i[0] not in "AEIOUaeiou":
            c = -1
            for q in i:
                if q not in "AEIOUaeiou":
                    c += 1
                if q in "AEIOUaeiou": break
            y += i[c+1:len(s)+1]+"a"+i[0:c+1]+"ay"+" "
    return y

def toEnglish(s):
    p = s.split()
    y = ""
    for i in p:
        if "way" in i:
            y += i[0:i.find("way")]+" "
        elif i.count("a")==2:
            cons = i[i.find("a")+1:i.find("ay")]
            y += cons+i[0:i.find("a")]+" "
        elif i.count("a")>=2:
            i = i[0:len(i)-2]
            c = i[i.rfind("a")+1:len(i)]
            y += c+i[0:i.rfind("a")]+" "
    return y 