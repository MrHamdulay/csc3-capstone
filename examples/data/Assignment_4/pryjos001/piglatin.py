def toPigLatin(s):
    
    #split sentence into seperate words
    wordlist = s.split()
    
    sentence=("")
    
    for i in wordlist:
        #wordlist[i][0] takes first letter of each word in sentence sequentially
        if i[0] in "aeiou":
            pig_word1 = i+"way"
            sentence+=pig_word1+" "
            
        else:
            for j in range (1,len(i)+1):
                if i[j] in "aeiou":
                    pig_word2 = i[j:]+"a"+i[:j]+"ay"
                    sentence+=pig_word2+" "
                    break
    sentence = sentence[:-1]
                
    return sentence

def toEnglish(s):
    
    wordlist = s.split()
    
    sentence = ("")
    
    for i in wordlist:
        if i[len(i)-3]=="w":
            eng_word1 = (i[:len(i)-3]+" ")
            sentence+=eng_word1
        
        else:
            for k in range(len(i)-3,-1,-1):
                if i[k] in "aeiou":
                    eng_word2 = (i[k+1:len(i)-2]+i[:k]+" ")
                    sentence+=eng_word2
                    break
    sentence = sentence[:-1]
    return sentence