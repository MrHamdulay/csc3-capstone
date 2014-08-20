def toPigLatin(s):
    s+=" "
    x="" #printable string
    start=0 #where to find word in string
    for i in range(0,len(s)):
        if s[i]==" ":
            x+=toPigLatinword(s[start:i])+" "
            start=i+1
        else:
            continue
    x=x[0:len(x)-1]
    return x

def toPigLatinword(s):
    if s[0] in "aeiou":
        return s+"way"
    else:
        for i in range(1,len(s)):
            if s[i] in "aeiou":
                x=s[i:len(s)+1]+"a"+s[0:i]+"ay"
                return x
        else:
            x="a"+s[0:len(s)]+"ay"
            return x

def toEnglishword(s):
    p=len(s)
    x=""
    if s[len(s)+1:len(s)-4:-1]=="yaw":
        return s[0:len(s)-3]
    else:
        s=s[0:len(s)-2]
        for i in range(len(s)-1, -1,-1):
            if s[i] not in "aeiou":
                x=s[i]+x
            elif s[i]=="a":
                p=i
                break    
            else:
                print("ERROR")
        return x+s[0:p]
            
def toEnglish(s):
    s+=" "
    x="" #printable string
    start=0 #where to find word in string
    for i in range(0,len(s)):
        if s[i]==" ":
            x+=toEnglishword(s[start:i])+" "
            start=i+1
        else:
            continue
    x=x[0:len(x)-1]
    return x