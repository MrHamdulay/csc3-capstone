#JNSJOH014
#Assignment 4 Question 3

def translate(s):
    if s[0] in ("aeiou"):
        s += "way"
        return s
    else:
        char = "a"
        i = 0
        while s[i] not in ("aeiou"):
            char+=s[i]
            i+=1
            if i==len(s):
                break
        s = s[i:]
        char+="ay"
        s+=char
        return s
    
    
def toPigLatin(s):
    new = ""
    s+=" "
    while True:
        space = s.find(" ")
        temp = s[0:space]
        new += translate(temp)+" "
        s = s[space+1:]
        if s.find(" ") == -1:
            break
    new = new[0:len(new)-1]
    return new


def reverse(a):
    if a.find("way") != -1:
        return a[:a.find("way")]
    else:
        a = a[:len(a)-2]
        i=len(a)-1
        cluster=""
        while a[i] != "a":
            cluster = a[i] + cluster
            i += -1
        a = a[0:i]
        a = cluster+a
        return a
    
    
def toEnglish(s):
    new = ""
    if s[len(s)-1] != " ":
        s+=" "
    while True:
        posspace = s.find(" ")
        temp = s[0:posspace]
        new += reverse(temp)+" "
        s = s[posspace+1:]
        if s.find(" ") == -1:
            break
    new = new[0:len(new)-1]
    return new