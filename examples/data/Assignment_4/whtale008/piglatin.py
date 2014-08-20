def toPigLatin(s):
    
    words = s.split(" ")
    ns = wordP(words[0])
    for word in words[1::]:
        ns = ns+" "+wordP(word)
    return ns
        
def toEnglish(s):
    words = s.split(" ")
    ns = wordE(words[0])
    for word in words[1::]:
        ns = ns+" "+wordE(word)
    return ns

    

def wordP(word):
    if word[0] in 'aeiou':
                nword = word+"way"
    else:
        count = 0
        for l in word:
            if (l  in "aeiou") or (l in "w"):
                break
            else:
                count+=1
                        
        nword = word[count::] + "a"+ word[:count:]+"ay"    

    return nword

def wordE(word):
    if word[len(word)-3] == 'w':
        nword = word[:len(word)-3:]
    else:
        word = word[:len(word)-2:]
        nword = word[word.rindex("a")+1::]+word[:word.rindex("a"):]
   
    return nword