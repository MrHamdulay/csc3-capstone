def toPigLatin (s): 
    VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")    
    c=""   
    x=s.split(" ")
    for s in x:    
        if s[0]in VOWELS:  
            c+=(s + "way"+" ")  
        else: 
            d=0
            for i in s:
                if i not in VOWELS:
                    d+=1
                    continue
                else:
                    break
            c+= (s[d:] +"a"+s[:d] + "ay"+" ")
    return c[:len(c)-1]
#toPigLatin(s)

def toEnglish (s):
    VOWELS=("a","e","i","o","u","A","E","I","O","U")
    C=""
    X=s.split(" ")
    for s in X:
        if s[:len(s)-4:-1]== "yaw":
            C+=s[:len(s)-3]+" "
        else:
            D=-3
            for i in reversed (s[:-3]):
                if i not in"a":
                    D-=1
                    continue
                else:
                    break
            C+=(s[D:-2]+s[:D-1]+" ")
    return(C)
#toEnglish("aaaaway aaabway aabaway aabbway abaaway ababway abbaway abbbway aaaabay aababay abaabay abbabay aaabbay ababbay aabbbay abbbbay")