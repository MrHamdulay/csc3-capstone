vowels = "aeiou"

def toPigLatin(s):
    bring = ""
    s = s.split()
    for i in s:
        index = (len(i) + 1)
        
        if i[0] in vowels:
            bring = bring + i + "way"
        else:
            for x in range(len(i)):
                if i[x] in vowels:
                    index = x
                    break
            bring = bring + i[index:] + "a" + i[:index] + "ay"
        bring = bring + " "
    return bring

def toEnglish(l):
    
    bring2 = ""
    index = 0
    l = l.split()
    
    for i in l:
        if i[-3] == "w":
            bring2 = bring2 + i[:-3]
            
        else:
            for j in range(len(i) - 3, -1, -1):
                if i[j] == "a":
                    index = j
                    break
            bring2 = bring2 + i[index+1:-2] + i[:index]
        bring2 = bring2+" "
    return bring2