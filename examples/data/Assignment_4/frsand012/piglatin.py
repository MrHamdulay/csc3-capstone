
def Latin(s):
    text = s.split(" ")
    x = s.count(" ") + 1   
    piglatin = ""
                         
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVWXYZ"    
    for i in range(0,x):
        word = text[i] + " " 
        if word[0] in vowels:
            piglatin += word[:-1] + "way" + " "
        elif word[0] in consonants:
            c = 0
            r = 1
            while word[c] in consonants:
                    newtext = word[r:-1] 
                    cons = word[:r]
                    r += 1
                    c += 1    
            piglatin += newtext + "a" + cons + "ay" + " "
    return piglatin

def English(s):
    text = s.split(" ")
    x = s.count(" ") + 1    
    english = ""                       
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvxyzBCDFGHJKLMNPQRSTVWXYZ"   
    for i in range(0,x):
        word = text[i] + " "
        if word[-4:] == "way ":
            english += word[0:-4] + " "
        elif word[0] in vowels:
            word = word[:-3]  
            r = len(word) - 1
            cons = ""
            while word[r] in consonants:
                    cons += word[r]
                    newword = word[:r]
                    r -= 1     
            english += cons[::-1] + newword[:-1] + " " 
    return english