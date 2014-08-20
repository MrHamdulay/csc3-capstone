def toPigLatin(s):
    acc='' #accumulator
    for i in s.split(" "):
        if i[0] in 'aeiou':   #if it starts wiht a vowel
            acc+=i+'way '
        else:
            for z in i:
                if z in 'aeiou':   #when the word hits a vowel
                    acc+=i[i.find(z):]+'a'+i[:i.find(z)]+'ay '
                    break
            else:
                acc+='a'+i+'ay '
    return acc[:len(acc)-1]
           

def toEnglish(s):
    acc=''
    rev=''
    for i in s.split(' '):
        if i[len(i)-3:]=='way':
            acc+=i[:len(i)-3]+' '
        else:
            rev=i[::-1][2:]
            for z in i:
                if z=='a':
                    acc+=(rev[rev.find('a')+1:]+rev[:rev.find('a')])[::-1]+' '
                    break
    return acc[:len(acc)-1]
            

    