def toPigLatin(s):
    new_s = ""
    new_w= ""
    vowels = ("a","e","i","o","u")
    for word in s.split():
        w=word
        if w[:1] in vowels:
            new_w= w + "way " #space after way
            new_s = new_s + new_w
        else:
            rem = ""
            cons= w[:1]
            length = len(w)
            i= 0
            for k in range(0,length):
                if w[k+1:k+2] in vowels:
                    rem= w[k+1:length]
                    break
                cons = cons + w[k+1:k+2]
                i=k+1  
            Adjust = "a"+ cons + "ay"
            rem= w[i+1:length]
            new_w= rem + Adjust
            new_s = new_s + new_w + " "          
    return new_s

def toEnglish(s):
    new_s = ""
    new_w= ""
    vowels = ("a","e","i","o","u")
    for word in s.split(): 
        w=word
        length = len(w)
        l = w.find("w")
        if "w" in w:
            new_w= w[:l]
            
        else:
            a= w.find("ay")
            sub= w[0:a]
            new_sub= ""
            length2= len(sub)
            i=0
            for k in range(length2-1,-1,-1):
                if sub[k:k+1] == "a":
                    i=k
                    break
                new_sub= new_sub + sub[k]
            rem= sub[0:i]
            sub_string = new_sub[::-1]
            new_w= sub_string +rem
            
        new_s = new_s + new_w + " "
    return new_s
