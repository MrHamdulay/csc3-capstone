def toPigLatin(d):
    acc=''
    for i in d.split(" "):
        if i[0] in 'aeiou':
            acc+=i+'way '
        else:
            for z in i:
                if z in 'aeiou':
                    acc+=i[i.find(z):]+'a'+i[:i.find(z)]+'ay '
                    break
            else:
                acc+='a'+i+'ay '                       
    return acc[:len(acc)-1]
def toEnglish(d):
    acc=''
    rev=''
    for i in d.split(" "):
        if i[len(i)-3:] == 'way':
            acc+=i[:len(i)-3]+' '
        else:
            rev = i[::-1][2:]
            for z in i:
                if z == 'a':
                    acc+=(rev[rev.find('a')+1:]+rev[:rev.find('a')])[::-1]+' '
                    break
    return acc[:len(acc)-1]

