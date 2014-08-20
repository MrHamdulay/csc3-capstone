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