def toPigLatin (x):
    
    x=x.split(' ')
    lengthList = len(x)
    vowel = ['a','e','i','o','u']
    xNew= ''
    for i in range(lengthList):
        iPos=0
        string=x[i]
        
        if string[0] in vowel:
            xNew= string+'way'
        else:
            for k in range(len(string)):
                if string[k] in vowel:
                    iPos=k
                    break
            if iPos!=0:
                xNew=string[iPos:]+'a'+string[:iPos]+'ay'
            elif iPos==0:
                xNew='a'+string+'ay'
        x[i]=xNew
        
    return ' '.join(x)

def toEnglish(x):
    sentence=x.split()
    newsentence=""
    for word in range(len(sentence)):
        if sentence[word][-3:]=="way":
            newsentence+=sentence[word][:-3]+" "
        elif sentence[word][-2:]=="ay":
            nWord=sentence[word][:-2]
            aPos=nWord.rfind("a")
            newsentence+=nWord[aPos+1:]+nWord[:aPos]+" "
    return(newsentence)

