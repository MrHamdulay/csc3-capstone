def toPigLatin(a):
    word=''
    for i in a.split(" "):
        if i[0] in "aeiou":
            word+=i+"way "
        else:
            for z in i:
                if z in "aeiou":
                    word+=i[i.find(z):]+"a"+i[:i.find(z)]+"ay "
                    break
            else:
                word+="a"+i+"ay "           
    return word[:len(word)-1]
def toEnglish(a):
    word=''
    reverse=''
    for i in a.split(" "):
        if i[len(i)-3:] == "way":
            word+=i[:len(i)-3]+" "
        else:
            reverse = i[::-1][2:]
            for z in i:
                if z == "a":
                    word+=(reverse[reverse.find('a')+1:]+reverse[:reverse.find('a')])[::-1]+' '
                    break
    return word[:len(word)-1]
