def toPigLatin(s):
    total=''
    for i in s.split():
        if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u":
            total+=i+"way "
        else:
            for j in i:
                if j in "aeiou":
                    pigl=i.find(j)
                    total+=i[pigl:]+"a"+i[0:pigl]+"ay "
                    break
    return total

def toEnglish(s):
    total=''
    for i in s.split():
        if i[-3:]=="way":
            eng=i[0:-3]
        else:
            pigl=i[0:-2]
            if pigl[-2:]=="bl" or pigl[-2:]=="th":
                eng=pigl[-2:]+pigl[0:-2]
                eng=eng[0:-1]
            else:
                eng=pigl[-1:]+pigl[0:-1]
                eng=eng[0:-1]
        total+=eng+' '
    return total
