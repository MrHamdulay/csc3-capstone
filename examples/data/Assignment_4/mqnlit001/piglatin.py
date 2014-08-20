def toPigLatin(s):
    word=''
    for i in s.split(" "):
        if i[0] in 'aeiou':
            word+=i+'way '
        else:
            for z in i:
                if z in 'aeiou':
                    word+=i[i.find(z):]+'a'+i[:i.find(z)]+'ay '
                    break
            else:
                word+='a'+i+'ay '           
    return word[:len(word)-1]
def toEnglish(s):
    word=''
    rev=''
    for i in s.split(" "):
        if i[len(i)-3:] == 'way':
            word+=i[:len(i)-3]+' '
        else:
            rev = i[::-1][2:]
            for z in i:
                if z == 'a':
                    word+=(rev[rev.find('a')+1:]+rev[:rev.find('a')])[::-1]+' '
                    break
    return word[:len(word)-1]

