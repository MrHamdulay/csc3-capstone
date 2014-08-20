def toPigLatin(s):
    string =""
    new_s = ""
    temp = ""
    var = True
    pos = 0
    vowel = "aeiou"
    while var == True:
        if s[0] in vowel:
            new_s += s[0:s.find(" ")] + "way "
        else: new_s += s[:s.find(" ")]+" "
        s = s[s.find(" ")+1:]
        if s.find(" ") == -1:
            var = False
            if s[0] in vowel:
                new_s += s + "way"
            else: new_s += s
    
    while var == False:
        pos = 0
        temp = ""
        if new_s.find(" ") != -1:
            while new_s[pos] not in vowel:
                temp  += new_s[pos]
                pos += 1
            if new_s[0] in vowel:
                string += new_s[0:new_s.find(" ")] + " "
            else:
                string += new_s[pos:new_s.find(" ")] + "a" + temp + "ay "
            new_s = new_s[new_s.find(" ")+1:]  
        else:
            while new_s[pos] not in vowel:
                temp  += new_s[pos]
                pos += 1
                if pos >= len(new_s): break
            if new_s[0] in vowel:
                string += new_s
            else:
                string += new_s[pos:] + "a" + temp + "ay"           
            var = True
    return string
            
            
                
def toEnglish(s):
    string =""
    pos = 3
    temp = ""
    new_s = ""
    var = True
    vowel = "aeiou"
    while var == True:
        if s.find(" ") == -1:
            var = False
            if s[-3:] == "way":
                new_s += s[0:-3]                
            else: new_s += s 
            break
        if s[s.find(" ")-3:s.find(" ")] == "way" :
            new_s += s[0:s.find(" ")-3] + " "
        else: new_s += s[:s.find(" ")]+" "
        s = s[s.find(" ")+1:]
        
    #print(new_s)
    while var == False:
        temp = ""
        pos = 3
        if new_s.find(" ") == -1:
            var = True
            if new_s[-2:] == "ay":
                while new_s[-pos] not in vowel:
                    temp += new_s[-pos]
                    pos +=1
                temp = temp[::-1]
                string += temp + new_s[0:-pos]
            else: string += new_s
            break
        if new_s[new_s.find(" ")-2:new_s.find(" ")] == "ay":
            while new_s[new_s.find(" ")-pos] != "a":
                temp += new_s[new_s.find(" ")-pos]
                pos +=1
            temp = temp[::-1]
            string += temp + new_s[0:new_s.find(" ")-pos]+ " "
        else: string += new_s[:new_s.find(" ")]+" "
        new_s = new_s[new_s.find(" ")+1:]
        
            
    return string