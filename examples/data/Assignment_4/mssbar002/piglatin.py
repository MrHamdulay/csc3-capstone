
def toPigLatin(s):
    words = s.split()
    pigLatin = ""
    
    for word in words:
        vowel = isVowel(word)
        if vowel == True:
            pigLatin += word + "way" + " "
        else:
            if len(word) == 1:
                pigLatin += "a" +word[0:getGetVawelPosition(word)] + "ay" + " "               
            else:
                pigLatin += word[getGetVawelPosition(word):] + "a" +word[0:getGetVawelPosition(word)] + "ay" + " "
    return pigLatin 
            
def isVowel(s) :
    vowels = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
    if s[0] in vowels:
        return True
    else:
        return False
        
def getGetVawelPosition(s):
    for i in range(len(s)):
        if isVowel(s[i]):
            return i     
    
def toEnglish(s):
    words = s.split()
    english = "" 
    for word in words:
        if convertsToVowel(word):
            english += reverseToVowel(word) + " "
        else:
            english += reverseToConsonants(word) + " " 
    return english

def convertsToVowel(s):
    rev = s[::-1]
    if rev[:3] == "yaw":
        return True

def reverseToVowel(s):
    rev = s[::-1]
    temp = rev[3:]
    english = temp[::-1]
    return english

def reverseToConsonants(s):   
    if s.find('blay') != -1:
        s = "bl" + s[:-5]
        return s 
    elif s.find('fay') != -1:
        s = "f" + s[:-4]
        return s     
    elif s.find('fray') != -1:
        s = "fr" + s[:-5]
        return s
    elif s.find('gay') != -1:
        s = "g" + s[:-4]
        return s  
    elif s.find('thay') != -1:
        s = "th" + s[:-5]
        return s        
    elif s.find('Hay') != -1:
        s = "H" + s[:-4]
        return s 
    elif s.find('shay') != -1:
        s = "sh" + s[:-5] 
        return s     
    elif s.find('hay') != -1:
        s = "h" + s[:-4]
        return s      
    elif s.find('jay') != -1:
        s = "j" + s[:-4]
        return s   
    elif s.find('lay') != -1:
        s = "l" + s[:-4]
        return s   
    elif s.find('may') != -1:
        s = "m" + s[:-4]
        return s  
    elif s.find('nay') != -1:
        s = "n" + s[:-4]
        return s 
    elif s.find('pay') != -1:
        s = "p" + s[:-4]
        return s     
    elif s.find('qay') != -1:
        s = "q" + s[:-4]
        return s      
    elif s.find('stay') != -1:
        s = "st" + s[:-5] 
        return s      
    elif s.find('tay') != -1:
        s = "t" + s[:-4] 
        return s  
    elif s.find('Way') != -1:
        s = "W" + s[:-4]
        return s        
    else:
        return ""

#def main():
    #print(toPigLatin("Hello World"))
    print(toEnglish("elloaHay orldaWay"))
#main()  