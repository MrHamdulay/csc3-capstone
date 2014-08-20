def toPigLatin(w):
    w=w+" @"
    string = ""
    while w != "@":
        word = w[:w.find(" ")]
        w = w[w.find(" ")+1:]
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            word = word + "way"
        else:
                a=word.find("a")
                
                if a==-1:a=10
                e=word.find("e")
                
                if e==-1:e=10
                i=word.find("i")
                
                if i==-1:i=10
                o=word.find("o")
                
                if o==-1:o=10
                u=word.find("u")
                
                if u==-1:u=10
                vowel = (min(a,e,i,o,u))
                
                if vowel==50:
                    word = "a"+ word + "ay"
                else:
                    word = word[vowel:]+"a"+word[:vowel]+"ay"
        string = string + " " + word
    string = string[1:]
    return( string)

def toEnglish(x):
    string = ""
    x=x+" ^"
    
    while x != "^":
        word = x[:x.find(" ")]
        x = x[x.find(" ")+1:]
        if word[(len(word)-3):]=="way":
                word=word[0:(len(word)-3)]
        else:
                word=word[:(len(word)-2)]
                a=word.rfind("a")
                word=word[(a+1):]+word[0:a]
        string = string + " " + word
    string = string[1:]
    return(string)