vowels = "a", "e", "i", "o", "u"

def pLatin(w):
    if w[0].lower() in vowels:
        return( w + "way")
    else:
        flag= True
        for i in range(len(w)):
            if w[i] in vowels:
                flag = False
        if flag == False:
            for i in range(len(w)):            
                if w[i].lower() in vowels:
                    return(w[i::] + "a" + w[:i:] + "ay")
        else:
            return "a" + w + "ay"
        

def eng(w):
    if w[len(w)-3::]=="way":
        return w[:len(w)-3:]
    else:
       w = w[:len(w)-2:]        
       for i in range(len(w))[::-1]:
           if w[i] == "a":
               return w[i+1::] + w[:i:]

def toPigLatin(s):
    words = s.split()
    newstr = ""
    for i in range(len(words)):
            newstr = newstr + pLatin(words[i]) + " "
    newstr=newstr[:-1:]
    return newstr
        
def toEnglish(s):
    words = s.split()
    newstr = ""
    for i in range(len(words)):
            newstr = newstr + eng(words[i]) + " "
    newstr=newstr[:-1:]
    return newstr
    
def yolo():
    s = toEnglish("elloaHay orldaWay")
    print(s)
    