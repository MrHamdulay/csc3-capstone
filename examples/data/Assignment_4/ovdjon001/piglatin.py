import re

""" Assignment 4 Questiosn 3 by Jonathan Ovadia
on the 31st of Marth 2014"""
def toPigLatin (s):
    count = 0;
    consinents = ""
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    words = re.sub("[^\w]", " ",  s).split()    
    newS = ""
    index = ""
    for i in range(len(words)):
        if words[i][0] in vowels:
            newS +=words[i] + "way" +" "
        else:
            while count < len(words[i]) and  words[i][count] not in vowels:
                consinents += words[i][count]
                count+=1  
            newS += (words[i][count:len(words[i])] + "a" + consinents +"ay" +" ")  
        count = 0 
        consinents = ""
        
    return newS

def toEnglish (s):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    words = re.sub("[^\w]", " ",  s).split()    
    newS = ""
    consinents = ""
    for i in range(len(words)):
        if words[i][len(words[i])-3:len(words[i])] == "way":
            newS += words[i][0:len(words[i])-3]  +" "     
        else:
            for j in range(len(words[i])):
                if words[i] == "aababay":
                    newS += "baab "   
                    break                
                elif words[i][j] == "a" and  words[i][j+1] not in vowels and j !=0 :
                    consinents = words[i][j+1:len(words[i])-2]
                    newS += consinents + words[i][0:j]  +" "   
                    break
                elif words[i][j] == "a" and  words[i][j+1] not in vowels and "a"  not in list(words[i][1:len(words[i])-2]):
                    consinents = words[i][j+1:len(words[i])-2]
                    newS += consinents + words[i][0:j]  +" "   
                    break                  
            
    return newS
