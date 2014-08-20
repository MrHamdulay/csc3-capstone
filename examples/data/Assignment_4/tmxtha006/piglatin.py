"""Hebert TEMA
TMXTHA006
3 APRIL 2014
this program converts a given English sentence into a PigLatin sentence or PigLatin to English"""

def toPigLatin(s):
    l_string=s.split()
    l_latin=[]
    for i in l_string:
        if ("aeiouAEIOU".find(i[0])!=-1):
            l_latin.append(i+"way")
        elif ("aeiou".find(i[0])==-1):
            index=[2*len(i)]
            for v in ("aeiouAEIOU"):
                val=i.find(v)
                if val!=-1:
                    index.append(val)
            s=min(index)
            word=i[s:]+"a"+i[:s]+"ay"
            l_latin.append(word)
    new_s=" ".join(l_latin)
    return new_s

def toEnglish(s):
    l_string=s.split()
    l_english=[]
    for i in l_string:
        if ("aeiouAEIOU".find(i[0])!=-1 and i[-3:]=="way"):
            l_english.append(i[:len(i)-3])
        elif ("aeiouAEIOU".find(i[0])!=-1 and i[-2:]=="ay"):
            w=i[::-1][2:].find("a")
            l_english.append(i[-(w+2):-2]+i[:-w-3])
    new_s=" ".join(l_english)
    return new_s


    

    
