#Conor O'Sullivan
#Converts English to Pig Latin & Visa Versa
#
def toEnglish(s):
    part = s.split()
    length = len(part)
    trans = ""
    for x in range(length):
        lenx = len(part[x])
        if part[x][-3] == "w":
            part[x] = part[x][0:lenx-3]
            trans += part[x] + " "
        else:
            part[x] = part[x][0:lenx-2]
            posa = -1
            start = ""
            while part[x][posa] != "a":
                start = part[x][posa] + start
                posa -= 1
                
            part[x] = (start + part[x])[0: len(part[x])-1]
            trans += part[x] + " "
    return trans



def toPigLatin(s):
    part = s.split()
    length = len(part)
    trans = ""
    for x in range(length):

        Vowel = isVowel(part[x][0:1])
        if  Vowel == True:
            part[x] += "way"
        else:
            end = "a"
            count = 0
            for con in range(len(part[x])):
                if isCon(part[x][con:(con+1)]) == False: break
                else:
                    end += part[x][con:(con+1)]
                    count +=1
                    
            part[x] = part[x][count:(len(part[x])+1)]  + end + "ay"  
        trans += part[x] + " "
    return trans

            
        
            

def isVowel(x):
    
    x = x.lower()
    vowel = False
    if x == 'a' or x == "e" or x== 'i' or x =="o" or x == "u":
        vowel = True
    else:
        vowel = False
    return vowel 

def isCon(x):
    x = x.lower()
    con = False
    if x == 'a' or x == "e" or x== 'i' or x =="o" or x == "u":
        con = False
    else:
        con = True
    return con   
