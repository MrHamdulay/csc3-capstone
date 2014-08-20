# Pig Latin
def toPigLatin(s):
    parts=s.split()
    #print(s)
    sentence=""
    i=""
    length = len(parts)
    for x in range(length):
        if isVowel(parts[x][0]) == True:
            parts[x] += "way"
            sentence += parts[x] + " "
        else: 
            count = 0
            end = "a"
            for con in parts[x]:
                    if isVowel(parts[x][count:count+1]) == True: 
        
                        break
                    
                    else:
                        end += parts[x][count:count+1]
                        count+=1
               

            parts[x] = parts[x][count:len(parts[x])+1] + end + "ay"
            sentence += parts[x] + " "
    #print(sentence)
        #sentence=sentence+i+" "
    return sentence

def toEnglish(s):
    
    s=s.split()
    #print(s)
    sentence=""
    i=""
    for x in range(len(s)): 

        if s[x][-3]== "w":
            
            i=s[x][0:-3]
            sentence += i + " "
        else:
            end = ""
            s[x] = s[x][0:(len(s[x])-2)]

            posa = -1
            start =""
            while s[x][posa] != "a":
                start = s[x][posa] + start
                posa -= 1
            s[x] = (start + s[x])[0: len(s[x])-1]

            sentence += s[x]+ " "
            
    
    #print(sentence)        
    return sentence
           
def isVowel(x):
    x = x.lower()
    vowel = False
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        vowel = True
    return vowel
        