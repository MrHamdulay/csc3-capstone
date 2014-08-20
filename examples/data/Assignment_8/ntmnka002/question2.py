def pairs(s, c):
    if len(s) == 0:
        return c
    else:
        if len(s) != 1:
        
            hold = s[0:2]
            
            if hold[0] == hold[1]:
                c += 1
            return pairs(s[1:], c)
        else: return pairs(s[1:], c)

#==================================================

word = input('Enter a message:\n')
c = 0
out = pairs(word, c)

print('Number of pairs:',out)