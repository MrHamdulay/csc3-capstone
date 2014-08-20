def toPigLatin(s):
    new_a = ""
    new_b= ""
    vowels = ("a","e","i","o","u")
    for word in s.split():
        w=word
        if w[:1] in vowels:
            new_a= w + "way " 
            new_b = new_b + new_a
        else:      #w = a, s = b
            remn = ""
            cons= w[:1]
            length = len(w)
            i= 0
            for k in range(0,length):
                if w[k+1:k+2] in vowels:
                    remn= w[k+1:length]
                    break
                cons = cons + w[k+1:k+2]
                i=k+1  
            Adj = "a"+ cons + "ay"
            remn= w[i+1:length]
            new_a= remn + Adj
            new_b = new_b + new_a + " "          
    return new_b

def toEnglish(s):
    new_b = ""
    new_a= ""
    vowels = ("a","e","i","o","u")
    for word in s.split(): 
        w=word
        length = len(w)
        l = w.find("w")
        if "w" in w:
            new_a= w[:l]
            
        else:
            a= w.find("ay")
            rep= w[0:a]
            new_rep= ""
            length2= len(rep)
            i=0
            for k in range(length2-1,-1,-1):
                if rep[k:k+1] == "a":
                    i=k
                    break
                new_rep= new_rep + rep[k]
            remn= rep[0:i]
            rep_string = new_rep[::-1]
            new_a= rep_string +remn
            
        new_b = new_b + new_a + " "
    return new_b


