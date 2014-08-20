def toPigLatin(s):
    s=s+" ##"
    sentence = ""
    while s != "##":
        word = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            word = word + "way"
        else:
            a=word.find("a")
            if a==-1:a=50
            e=word.find("e")
            if e==-1:e=50
            i=word.find("i")
            if i==-1:i=50
            o=word.find("o")
            if o==-1:o=50
            u=word.find("u")
            if u==-1:u=50
            vowel = (min(a,e,i,o,u))
            if vowel==50:
                word = "a"+ word + "ay"
            else:
                word = word[vowel:]+"a"+word[:vowel]+"ay"
        sentence = sentence + " " + word
    sentence = sentence[1:]
    return sentence

def toEnglish(s):
    s=s+" ##"
    sentence = ""
    while s != "##":
        word = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if word[(len(word)-3):]=="way":
            word=word[:(len(word)-3)]
        else:
            word=word[:(len(word)-2)]
            a=word.rfind("a")
            word=word[(a+1):]+word[:a]
        sentence = sentence + " " + word
    sentence = sentence[1:]
    return sentence