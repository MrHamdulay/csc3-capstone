def toPigLatin(s):
    s=s+" ##"
    sent = ""
    while s != "##":
        w = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if w[0]=="a" or w[0]=="e" or w[0]=="i" or w[0]=="o" or w[0]=="u":
            w = w + "way"
        else:
            a=w.find("a")
            if a==-1:
                a=50
            e=w.find("e")
            if e==-1:
                e=50
            i=w.find("i")
            if i==-1:
                i=50
            o=w.find("o")
            if o==-1:
                o=50
            u=w.find("u")
            if u==-1:
                u=50
            vow = (min(a,e,i,o,u))
            if vow==50:
                w = "a"+ w + "ay"
            else:
                w = w[vow:]+"a"+w[:vow]+"ay"
        sent = sent + " " + w
    sent = sent[1:]
    return sent

def toEnglish(s):
    s=s+" ##"
    sent = ""
    while s != "##":
        w = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if w[(len(w)-3):]=="way":
            w=w[:(len(w)-3)]
        else:
            w=w[:(len(w)-2)]
            a=w.rfind("a")
            w=w[(a+1):]+w[:a]
        sent = sent + " " + w
    sent = sent[1:]
    return sent