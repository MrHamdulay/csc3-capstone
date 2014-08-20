def toPigLatin(s):
    sent = ""
    s=s+" ##"
    while s != "##":
        word = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            word = word + "way"
        sent = sent + " " + word
    sent = sent[1:]
    return sent            
    

def toEnglish(s):
    sent = ""
    s=s+" ##"
    while s != "##":
        word = s[:s.find(" ")]
        s = s[s.find(" ")+1:]
        if word[(len(word)-3):]=="way":
            word=word[:(len(word)-3)]
        else:
            word=word[:(len(word)-2)]
            a=word.rfind("a")
            word=word[(a+1):]+word[:a]
        sent = sent + " " + word
    sent = sent[1:]
    return sent