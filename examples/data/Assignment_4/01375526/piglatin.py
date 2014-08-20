# module piglatin
# hs

def PLword (s):
    conson = 0
    while (conson<len(s) and (s[conson].lower() not in ['a','e','i','o','u'] )):
        conson=conson+1
    if conson==0:
        return s+"way"
    else:
        return s[conson:] + "a" + s[:conson] + "ay"    
    return s

def ENword (s):
    if (s[-3:] == "way"):
        return s[:-3]
    else:
        s = s[:-2]
        conson = 0
        while (conson<(len(s)-1) and (s[-conson-1].lower() not in ['a','e','i','o','u'] )):
            conson=conson+1
        return s[-conson:] + s[:-conson-1]

def convert (s, direction):
    new = ""
    while (s):
        cha = s[0]
        s = s[1:]
        if (cha != " "):
            word = cha
            while ((s) and (s[0]!=" ")):
                word = word + s[0]
                s = s[1:]
            newWord = new
            if direction == 1:
                newWord = PLword (word)
            else:
                newWord = ENword (word)    
            new = new + newWord
        else:
            new = new + cha
#        print (s + "|" + new)
    return new

def toPigLatin (s):
    return convert (s, 1)

def toEnglish (s):
    return convert (s, 2)

#a = "the quick green fox jumps over the lazy dog"
#a = "a b aa ab ba bb aaa aab aba abb baa bab bba bbb aaaa aaab aaba aabb abaa abab abba abbb baaa baab baba babb bbaa bbab bbba bbbb"
#a = "a w aa aw wa ww aaa aaw awa aww waa waw wwa www"
#b = toPigLatin (a)
#c = toEnglish (b)

#print (a)
#print (b)
#print (c)
