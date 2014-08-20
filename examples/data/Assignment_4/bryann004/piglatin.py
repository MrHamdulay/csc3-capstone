def toPigLatin(s):
    out=""
    for word in s.split():

        if word[0] in "aeiou" or word[0] in "AEIOU":
            out += word + "way "
        else:
            end=""
            k=0
            for i in word:
                if i in "aeiou":
                    break                
                end += i
                k += 1
            out += word[k:] + "a" + end + "ay "
        
        
    out = out[:-1]
    return out

    
def toEnglish(s):
    out=""
    for word in s.split():
        word = word[:-2]
        if word[-1] == "w": #and word[-2] != "a":
            out += word[:-1] + " "
        else:
            strt=""
            k=0
            rev=word[::-1]
            for i in rev:
                if i in "a":
                    break
                strt += i
                k += 1
            out += strt[::-1] + word[:-(k+1)] + " "
    out = out[:-1]
    return out
