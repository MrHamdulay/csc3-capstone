def toPigLatin(s):
    y=xx[0:1]
    if y=="a" or y=="e" or y=="i" or y=="o" or y=="u":
        return (xx+"way")
    
def toEnglish(s):
    vowel=("aeiou")
    t=s.find(" ")
    r=s[0:t] 
    while True:
        t=s.find(" ")
        r=s[0:t]         
        if r[0] in vowel:
            s = s[t+1:]
            return (r + "way")
        else:
            for i in range(len(r)):
                if r[i] in vowel:
                    s = s[t+1:]
                    return (r[i:] +"a" +r[:i] +"ay")
                break
            