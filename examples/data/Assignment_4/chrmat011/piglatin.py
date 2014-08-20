def toPigLatin(s):
    vowels='aeiou'
    word = s.split()
    for p in range(len(word)):
        if vowels.count(word[p][0])>0:
            word[p] = word[p] + 'way'
        else:
            t=['']*(len(word[p])+1)
            for i in range(len(word[p])):
                t[i]=word[p][i]
            t[len(word[p])]='a'    
            while not vowels.count(t[0])>0:
                e=t[0]
                for i in range(len(t)-1):
                    t[i]=t[i+1]
                t[len(t)-1]=e
            word[p]=''
            for i in range(len(t)):
                word[p]+=t[i]
            word[p] = word[p] + 'ay'
    return ' '.join(word)

def toEnglish(s):
    word = s.split()
    for i in range(len(word)):
        if word[i].count('w') > 0:
            word[i] = word[i][0:len(word[i])-3]
        else:
            word[i] = word[i][0:len(word[i])-2]
            cons = ''
            while word[i][len(word[i])-1] != 'a':
                cons+=word[i][len(word[i])-1]
                word[i]=word[i][0:len(word[i])-1]
            word[i] = cons[::-1]+word[i][0:len(word[i])-1]
    return ' '.join(word)

