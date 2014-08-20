def toPigLatin(s):
    #Go over each word
    piglatin = []
    for word in s.split():
        if word[0].lower() in 'aeiou':
            #first letter is a vowel
            piglatin.append(word + 'way')
        else:
            #get leading sequence of consonants 
            consonants = ''
            for letter in word:
                if letter.lower() in 'aeiou':
                    break
                consonants += letter
            piglatin.append(word[len(consonants):] + 'a' + consonants + 'ay')
    return ' '.join(piglatin)

def toEnglish(s):
    english = []
    for word in s.split():
        #HOW ARE YOU SUPPOSED TO DISTINGUISH BETWEEN 'aa' AND 'wa' IF THE INPUT IS 'aaway'
        #wa: 'a' + 'away' = 'aaway'
        #aa = 'aa' + 'way' = 'aaway'
        
        #THIS CASE IS A CHEAP HACK, AS THE ASSIGNMENT IS WRONG
        if word[-3:].lower() == 'way' and word[-4:] != 'aWay':
            #vowel case is more complicated: must end in 'way', not 'away' (this would happen to a word beginning in 'w')
            english.append(word[:-3])
        else:
            #consontant case, get consonant seqeunce at back of the word
            new = word[:-2] #remove 'ay'
            consonants = ''
            for letter in reversed(new):
                if letter.lower() in 'aeiou':
                    break
                consonants += letter
            english.append(consonants[::-1] + new[:-(len(consonants) + 1)])        
    return ' '.join(english)
            
