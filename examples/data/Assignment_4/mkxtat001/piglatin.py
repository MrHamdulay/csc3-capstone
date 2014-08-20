#Tato Moaki MKXTAT001
#Program to convert string either from pig latin to english or the other around
#Assignment4 question3
def isVowel(word):
    #check whether passed character is a vowel or not
    if(word == "a" or word == "e" or word == "i" or word == "o" or word == "u"):
        return True
    else:
        return False
    
def toPigLatin(s): 
    #converts a passed string to a pig latin string
    myStringList = s.split()
    emptyString = ""
    for i in myStringList:
        if(isVowel(i[0])):
            emptyString += ( i +"way")
            emptyString += " "
            
        else:
            for j in range(len(i)): #iterate through the sequence of string 
                if(isVowel(i[j])): #if isVowel returns true
                    i = (i[j:]+"a"+ i[0:j] + "ay")
                    emptyString +=(i)
                    emptyString += " "
                    break
            else:
                emptyString += ("a"+i+"ay")
                emptyString += " "
                break
    return(emptyString)
    
                
def toEnglish(s):
    #function converts pig latin string to english
    list = s.split()
    emptyString =""
    for i in list:
        if(i[-3:] == "way"):
            i = i.replace(i[-3:],"")
            emptyString+=(i)  
            emptyString +=" "
        else:
            i = i.replace(i[-2:],"")             
            for j in range ((len(i)-1),-1,-1):
                if(isVowel(i[j])):
                    i = i[j+1:]+i[0:j]
                    emptyString+=(i) 
                    emptyString += " "
                    break
    return(emptyString)
        
                    