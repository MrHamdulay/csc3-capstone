def findfirstvowel(word):
    for position, letter in enumerate(word):
        if letter in ('a', 'e', 'i', 'o', 'u'):
            return position
    return -1

def ConvertToP(word):
    firstletter = word[0]
    if firstletter in ('a', 'e', 'i', 'o', 'u'):
        return word + "way "
    else:
        vowelposition = findfirstvowel(word)
        if vowelposition == -1: return "a" + word + "ay "
        else: return word[vowelposition:] + "a" + word[:vowelposition] + "ay "

def toPigLatin(s):
    wordstring = s.split(" ")
    pigsentence = ""   
    for word in wordstring:
        pigsentence = pigsentence + ConvertToP(word)    
        pigesentence = pigsentence + " "
    return pigsentence[:len(pigsentence)-1]

def a_pos(word):
    count = 0
    pos1 = 0
    pos2 = 0
    for i in range(len(word)-1,-1,-1):
        if word[i] == "a":count+=1
        if count == 2:
            pos1=i
            count+=1
    for i in range(len(word)-1,-1,-1):
        if word[i] == "a":
            pos2 = i
            break
    return pos1, pos2
    
def ConvertToE(word):
    if word[len(word)-3] == "w": return word[:len(word)-3]
    else:
        pos1, pos2 = a_pos(word)
        return word[pos1+1:pos2] + word[:pos1]
    
def toEnglish(s):
    wordstring = s.split(" ")
    engsentence = ""   
    for word in wordstring:
        engsentence = engsentence + ConvertToE(word)    
        engsentence = engsentence + " "
    return engsentence[:len(engsentence)-1]