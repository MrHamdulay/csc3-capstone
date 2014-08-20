#Question 3
#Converting from and to piglatin
#By:Dean de Haast

#Converting English to PigLatin
def toPigLatin(s):
    sentance=""
    for word in s.split():
        cons = ""
        curword = word
        i=0
        rest=""
            
        if curword[0] in "aeiou" or curword[0] in "AEIOU":
            curword = curword+"way"
            sentance= sentance+curword+" "
        else:
            for x in word:
                if x in "aeiou" or x in "AEIOU":
                    rest+=(word[i:])                                   
                    break
                else: 
                    if i == (len(word)-1):
                        rest=""
                        cons=word
                        break
                                                                                      
                    cons = cons+x
                i +=1
            sentance = sentance+ rest+"a"+cons+"ay"+" " 

    return(sentance)


def toEnglish(s):
    sentance=""

    for word in s.split():
        count= 0
        temp=""
        wordrvs=""
        wordrvs=word[::-1]
        if wordrvs[2] =="w":
            wordrvs=wordrvs[3:]
            word2=wordrvs[::-1]
        else:
            wordrvs=wordrvs[2:]
            for x in wordrvs:
                count +=1
                if x =="a":
                    wordrvs=wordrvs[count:]                   
                    wordrvs+=temp                    
                    word2=wordrvs[::-1]
                    
                    break
                else:
                    temp +=x
        sentance =sentance+word2+" "
                
                
                    
    return(sentance)