infn = input('')

outfn = 'output.txt'

wid = 40

import math
#======================================================
#Read to TF
#f = open(infn, 'r')

string = infn

def lines(s, o):
    b = ''
    pos = 0
    
    if len(s) == 0:
        return ''
    elif (len(s)) > 0 and (len(s) <= 40):
        return (o + s)
    elif len(s) > 40:
        
        p = s[0:40]
        for k in range(-1, -40, -1):
            
            if p[k] == ' ':
                pos = k
                break
              
        pos = pos + 40
        
        o += s[0: pos + 1] + '\n'
        s = s[pos + 1:]
        return lines(s, o)
        
out = ''

output = lines(string, out)

print(output)

#======================================================
#This part works properly - just remove these quotes
file = open(outfn, 'w')
file.write(string)
file.close()