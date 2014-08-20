#Pig Latin translator
#Kavir Ranchod  -   RNCKAV001
#01/04/2014

vowels = ('aeiou')

def toPigLatin(s):
    sentence=s.split(" ")
    translation=""
    for word in sentence:
        if word[0] in vowels:
            translation+=(word+"way"+" ")
        else:
            VI=0
            for letter in word:
                if letter not in vowels: 
                    VI+=1
                    continue
                else: 
                    break
            translation+=(word[VI:]+"a"+word[:VI]+"ay"+" ")
    return translation[:len(translation) - 1]

def toEnglish(s):
    sentence=s.split(" ")
    translation=""
    for word in sentence:
        if word[:len(word)-4:-1]=='yaw':
            translation+=word[:len(word)-3]+" "
        else: 
            noay=word[:len(word)-2]
            consonants=noay.split("a")[-1]
            consonantsremoved=noay[:len(noay)-(len(consonants)+1)]
            translation+=consonants+consonantsremoved+" "
    return translation