def toPigLatin(s):
    total=''
    for i in s.split():
        if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u":
            total+=i+"way "
        else:
            for j in i:
                if j in "aeiou":
                    a=i.find(j)
                    total+=i[a:]+i[0:a]+"ay "
                    break
    return total

def toEnglish(s):
    total=''
    for i in s.split():
        if i[-3:]=="way":
            b=i[0:-3]
        else:
            a=i[0:-2]
            if a[-2:]=="bl" or a[-2:]=="th":
                b=a[-2:]+a[0:-2]
            else:
                b=a[-1:]+a[0:-1]
        total+=b+' '
    return total

