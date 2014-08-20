def toPigLatin(s):
    ben=''
    for i in s.split(" "):
        if i[0] in "aeiou":
            ben+=i+"way "
        else:
            for z in i:
                if z in "aeiou":
                    ben+=i[i.find(z):]+"a"+i[:i.find(z)]+"ay "
                    break
            else:
                ben+="a"+i+"ay "           
    return ben[:len(ben)-1]
def toEnglish(s):
    ben=''
    ben1=''
    for i in s.split(" "):
        if i[len(i)-3:] == "way":
            ben+=i[:len(i)-3]+" "
        else:
            ben1 = i[::-1][2:]
            for z in i:
                if z == "a":
                    ben+=(ben1[ben1.find('a')+1:]+ben1[:ben1.find('a')])[::-1]+' '
                    break
    return ben[:len(ben)-1]
