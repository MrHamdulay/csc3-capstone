#Piglatin program 
#convert from english to piglatin and back

def toPigLatin(s):
    word=''
    for i in s.split(" "):
        if i[0] in 'aeiou':
            word+=i+'way '
        else:
            for c in i:
                if c in 'aeiou':
                    word+=i[i.find(c):]+'a'+i[:i.find(c)]+'ay '
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
            for c in i:
                if c == 'a':
                    word+=(rev[rev.find('a')+1:]+rev[:rev.find('a')])[::-1]+' '
                    break
    return word[:len(word)-1]

