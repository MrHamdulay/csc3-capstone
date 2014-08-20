def toPigLatin(s):
    words = s.split()
    sentence = []
    for word in words:
        if(word[0] in 'aeiouAEIOU'):
            sentence.append(word+"way")    
        else:
            word = word+"a"
            while (word[0] not in "aeiouAEIOU"):
                word = "".join((word[1:], word[0]))
            sentence.append(word+"ay")
    return ' '.join(sentence)

def toEnglish(s):
    words = s.split()
    sentence = []

    for word in words:
        newLength = len(word)
        if(word[-3] == 'w'):
            word = word[0:newLength-3]
        else:
            newLength2 = len(word)
            word2 = word[0:newLength2-2]
            index = word2.rfind("a")
            partWord1 = word[newLength2-3:index:-1]
            partWord2 = word[:index]
            word = partWord1[::-1]+partWord2
            
        sentence.append(word)
        
    return ' '.join(sentence)