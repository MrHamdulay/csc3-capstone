def toPigLatin (s):
    
    s = s.split()
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    sNew = ''
    string = ''
    for i in range(len(s)):
        c = 0
        string = s[i]
        if string[0] in vowels:
            sNew = string+'way'
        else:
            for k in range(len(string)):   
                if string[k] in vowels:
                    c = k 
                    break
            if c!= 0:
                sNew = string[c:] + 'a' + string[:c] + 'ay'
            elif c == 0:
                sNew = 'a' + string + 'ay'
        s[i] = sNew           
    return ' '.join(s)

def toPigLatin2(s):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    output = ''
    c = 0
    s = s.split()
    while c<len(s):
        if c!=0:
            output = output + ' '
            if s[c][0] in vowels:
                output = output + s[c] + 'way'
            else:
                t=0
                for y in range(len(s[c])):
                    if s[c][t] in vowels:
                        break
                    else:
                        t+=1
                output = output + s[c][t::] + 'a' + s[c][0:t:1] + 'ay'
        c+=1
    return output   
    
def toEnglish(s):
    output = ''
    c=0
    s=s.split()
    while c<len(s):
        if c!=0:
            output = output + ' '
        if s[c][-1:-4:-1]=='yaw':
            output = output + s[c][0:-3:1]
        else:
            x=-3
            while s[c][x]!='a':
                x=x-1
            output = output + s[c][x+1:-2:1] + s[c][0:x:1]
        c+=1
    return output
                