__author__ = 'George'
def word(s):
    if s[0] in ("a","e","i","o","u"):
        s += "way"
        return s
    else:
        i = 0
        cons = "a"
        while s[i] not in ("a","e","i","o","u"):
            cons += s[i]
            i += 1
            if i == len(s):
                break
        s = s[i:]
        cons += "ay"
        s = s+cons
        return s
def toPigLatin(s):
    new = ""
    s += " "
    while True:
        space = s.find(" ")
        woord = s[0:space]
        new += word(woord)+" "
        s = s[space+1:]
        if s.find(" ") == -1:
            break
    new = new[0:len(new)-1]
    return new
def dec(a):
    if a.find("way") != -1:
        return a[:a.find("way")]
    else:
        a = a[:len(a)-2]
        i=len(a)-1
        cons=""
        while a[i] != "a":
            cons = a[i] + cons
            i += -1
        a = a[0:i]
        a = cons+a
        return a
def toEnglish(s):
    new = ""
    if s[len(s)-1] != " ":
        s += " "
    while True:
        space = s.find(" ")
        woord = s[0:space]
        new += dec(woord)+" "
        s = s[space+1:]
        if s.find(" ") == -1:
            break
    new = new[0:len(new)-1]
    return new