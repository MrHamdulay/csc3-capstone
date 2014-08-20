def toPigLatin(s):
    x = ''
    for i in s.split(" "):
        if i[0] in 'aeiou':
            x+=i+'way '
        else:
            for y in i:
                if y in 'aeiou':
                    x+=i[i.find(y):]+'a'+i[:i.find(y)]+'ay '
                    break
            else:
                x+='a'+i+'ay '           
    return x[:len(x)-1]
def toEnglish(s):
    x = ''
    y = ''
    for i in s.split(" "):
        if i[len(i)-3:] == 'way':
            x+=i[:len(i)-3]+' '
        else:
            y = i[::-1][2:]
            for z in i:
                if z == 'a':
                    x+=(y[y.find('a')+1:]+y[:y.find('a')])[::-1]+' '
                    break
    return x[:len(x)-1]

#x=input("(E)nglish or (P)ig Latin?\n")
#y=x.[:1]
#if y=="E":
    #words=input("Enter an English sentence:\n")
    #print("Pig-Latin:")
    #toPigLatin(s)
    
#elif y=='P':
    #words=input("Enter a Pig Latin sentence:\n")
    #print("English:")
    #toEnglish(s)

