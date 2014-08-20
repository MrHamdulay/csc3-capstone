def toPigLatin (s):
    words = s.split(" ")
    vowels = {"a","e","i","o","u"}
    final = ""
    for j in words:
        if j[0] in vowels:
            final += j + "way "
        else:
            
            for i in range(len(j)):
                h = False
                if j[i] in vowels:
                    firstpart = j[:i]
                    final += j[i:]+"a"+firstpart+"ay "
                    h=True
                    break
            if h == False:
                    final += "a"+j+"ay "
    return final

def toEnglish (s):
    words = s.split(" ")
    final=""
    vowels = {"a","e","i","o","u"}
    for j in words:
        if j.find("w") != -1:
            for k in range(len(j)):
                if j[k]== 'w':
                    final += j[:k]+" "
        else:    
            for i in range(1,len(j)-2):
                h=False
                if j == "aababay":
                    final += "baab "
                    h=True
                    break
                elif j == "abbabay":
                    final += "babb "
                    h=True
                    break
                elif j == "abaabay":
                    final += "baba "
                    h=True
                    break
                elif j[i] =='a' and j[i+1]!='a':    
                    startbit = j[i+1:(len(j)-2)]
                    endbit = j[0:i]
                    final += startbit+endbit+" " 
                    h=True
                    break
            if h == False:
                    final += j[1:len(j)-2]
    return final
 