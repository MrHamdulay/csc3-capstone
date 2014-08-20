def toPigLatin(sent):
    total=''
    for word in sent.split():
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            new_sen+=word+"way "
        else:
            for pie in word:
                if pie in "aeiou":
                    a=word.find(pie)
                    new_sen+=word[a:]+"a"+word[0:a]+"ay "
                    break
    return new_sen

def toEnglish(sent):
    new_sen=''
    for word in sent.split():
        if word[-3:]=="way":
            b=word[0:-3]
        else:
            a=word[0:-2]
            if a[-2:]=="bl" or a[-2:]=="th":
                b=a[-2:]+a[0:-2]
            else:
                b=a[-1:]+a[0:-2]
        new_sen+=b+' '
    return new_sen