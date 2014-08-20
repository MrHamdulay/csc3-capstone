def toPigLatin(s):
    sentance=s.split()
    l=len(s)
    consonants = ''
    index=0
    piglatin=''
    
    for word in sentance:
        
        if vowelfinder(word[0]): 
            word = word+'way' 
        else:
            index=0
            while not vowelfinder(word[index]):
                index += 1
                if not index < len(word):
                    break
            word = word[index:l]+'a'+ word[:index] + 'ay'
        piglatin += word + ' '
    return piglatin
        

def vowelfinder(character):
        return character in 'aeiouAEIOU'

def toEnglish(s):
    sentance = s.split()
    english = ''
    
    for word in sentance:
        if word[-3]=='w': #to get rid of the way
                english+=word[:len(word)-3] + ' '
        else:
                word = word[:len(word)-2]
                cons = len(word)-word[::-1].find('a')
                word = word[cons:]+word[:cons-1]
                english += word + ' ' #adds a space between words
    return english  
    

