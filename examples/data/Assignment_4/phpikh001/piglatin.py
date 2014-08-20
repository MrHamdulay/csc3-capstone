#Ikhlaas Pohplonker
#1April 214

#return the Pig Latin string for a given English string
def toPigLatin (s):
    Vowels = ['a','e','i','o','u','A','E','I','O','U']
    s=s.split()
    language_pig=""
    for i in (s):
        if i[0] in Vowels:
            i=i+'way'
            language_pig=language_pig+i+" "   
        else:
            i=i+'a'
            while i[0] not in Vowels:
                i=i[1:] + i[0]
            i=i+'ay'
            language_pig=language_pig+i+" " 
    return language_pig 

#return the English string for a given Pig Latin string
def toEnglish (s):
    s=s.split()
    English=""
    for i in s:
        if i[-1:-4:-1] == 'yaw': 
            i=i[0:len(i)-3]
            English=English+i+" "
        else:
            i = i[0:len(i)-2]
            while i[-1] != 'a':
                i=i[-1] + i[0:len(i)-1]
            i=i[0:len(i)-1]
            English=English+i + " "       
    return English
