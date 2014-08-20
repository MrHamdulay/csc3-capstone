def toPigLatin(s):
    ac=''
    for i in s.split(" "):
        if i[0] in "aeiou":
            ac+=i+"way "
        else:
            for z in i:
                if z in "aeiou":
                    ac+=i[i.find(z):]+"a"+i[:i.find(z)]+"ay "
                    break
            else:
                ac+="a"+i+"ay "           
    return ac[:len(ac)-1]
def toEnglish(s):
    ac=''
    rev=''
    for i in s.split(" "):
        if i[len(i)-3:] == "way":
            ac+=i[:len(i)-3]+" "
        else:
            rev = i[::-1][2:]
            for z in i:
                if z == "a":
                    ac+=(rev[rev.find('a')+1:]+rev[:rev.find('a')])[::-1]+' '
                    break
    return ac[:len(ac)-1]
