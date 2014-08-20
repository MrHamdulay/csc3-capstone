def toPigLatin(k):
    k=k+" ##"
    sent = ""
    while k != "##":
        wor = k[:k.find(" ")]
        k = k[k.find(" ")+1:]
        if wor[0]=="a" or wor[0]=="e" or wor[0]=="i" or wor[0]=="o" or wor[0]=="u":
            wor = wor + "way"
        else:
            a=wor.find("a")
            if a==-1:a=50
            e=wor.find("e")
            if e==-1:e=50
            i=wor.find("i")
            if i==-1:i=50
            o=wor.find("o")
            if o==-1:o=50
            u=wor.find("u")
            if u==-1:u=50
            vow = (min(a,e,i,o,u))
            if vow==50:
                wor = "a"+ wor + "ay"
            else:
                wor = wor[vow:]+"a"+wor[:vow]+"ay"
        sent = sent + " " + wor
    sent = sent[1:]
    return sent

def toEnglish(k):
    k=k+" ##"
    sent = ""
    while k != "##":
        wor = k[:k.find(" ")]
        k = k[k.find(" ")+1:]
        if wor[(len(wor)-3):]=="way":
            wor=wor[:(len(wor)-3)]
        else:
            wor=wor[:(len(wor)-2)]
            a=wor.rfind("a")
            wor=wor[(a+1):]+wor[:a]
        sent = sent + " " + wor
    sent = sent[1:]
    return sent