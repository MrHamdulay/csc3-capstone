#aSSIGNMENT 4
#NQKITU001
def toPigLatin(s):
    words =s.split(" ")
    output = ""
    length =len(words)
    for i in range(length):
        if("aeiou".find(words[i][0:1]) != -1):
            words[i] = words[i] + "way"
        else:
            vpos = -1
            for j in range(len(words[i])):
                if("aeiou".find(words[i][j]) != -1):
                    vpos = j
                    break
            if(vpos == -1):
                words[i] = "a" + words[i] + "ay"
            else:
                part1 = words[i][0:vpos]
                part2 = words[i][vpos:]
                words[i] = part2 + "a" + part1 + "ay"
            
    for k in range(length):
        output += words[k] + " "
    return output 

def toEnglish(s):
    words = s.split(" ")
    output = ""
    length = len(words)
    for i in range(length):
        if(words[i].find("way") != -1):
            words[i]= words[i].replace("way", "")
        else:
            if(words[i].find("ay") != -1):
                j = words[i].replace("ay", "")
                parts = j.rsplit("a",1)
                if(len(parts) >= 1):
                    words[i] = parts[1] + parts[0]                
                    words[i] = words[i]
            else:
                words[i] = words[i]
    for k in range(length):
        output += words[k] + " "
    return output              
            
    