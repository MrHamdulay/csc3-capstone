def toPigLatin(s):
    newstr = ''
    # count words
    words = 1
    for i in range(len(s)):
        if s[i] == ' ':
            words += 1
    # index sentance
    string = s.split(' ')        
    for i in range(words):
        word = string[i]
        # vowel path
        if word[0] in 'aeiou':
            word += 'way'
        else:
            # consonants path
            k =0
            for c in word[:]:
                if c not in 'aeiou':
                    k +=1
                else: break
            word = word[k:len(word)] + 'a' + word[0:k] + 'ay'
        # check if last word for extra space issue
        if i == words:
            newstr += word
        else : newstr += word + ' '
        
    return newstr 

def toEnglish(s):
    string = s.split()
    newstr = ''
    for word in range(len(string)):
        if string[word][-3:] == 'way':
            newstr += string[word][:-3] + ' '
        elif string[word][-2:] == 'ay':
            nWord  = string[word][:-2]
            aPos =nWord.rfind("a") #rfind locates the position of a character from the right
            newstr += nWord[aPos+1:] + nWord[:aPos] + " "
    return newstr
            
            
            
    
    

    
            
     
