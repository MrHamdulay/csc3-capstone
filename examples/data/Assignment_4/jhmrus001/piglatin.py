def toPigLatin(q):
    g = ''
    for i in q.split(" "):
        if i[0] in 'aeiou':
            g+=i+'way '
        else:
            for y in i:
                if y in 'aeiou':
                    g+=i[i.find(y):]+'a'+i[:i.find(y)]+'ay '
                    break
            else:
                g+='a'+i+'ay '           
    return g[:len(g)-1]
def toEnglish(q):
    g = ''
    y = ''
    for i in q.split(" "):
        if i[len(i)-3:] == 'way':
            g+=i[:len(i)-3]+' '
        else:
            y = i[::-1][2:]
            for z in i:
                if z == 'a':
                    g+=(y[y.find('a')+1:]+y[:y.find('a')])[::-1]+' '
                    break
    return g[:len(g)-1]
