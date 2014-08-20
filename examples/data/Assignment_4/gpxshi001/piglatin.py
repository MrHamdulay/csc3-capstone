#Shivan Gopee
#2/4/2014
#Q3

def toPigLatin(D):
    
    conversion=''
    words= D.split()
    vowels='aeiouAEIOU'
    
    for word in words:
        if word[0] in vowels:
            conversion+= str(word) + 'way '

        elif word.find('a') == -1 and word.find('e') == -1 and word.find('i') == -1 and word.find('o') == -1 and word.find('u') == -1 and word.find('A') == -1 and word.find('E') == -1 and word.find('I') == -1 and word.find('O') == -1 and word.find('U') == -1:
            conversion+= 'a' + word[::] + 'ay '
        else:
            for char in word:
                if char in vowels:
                    conversion+= word[word.find(char):] +'a' + word[:word.find(char)] + 'ay '
                    break        
        
    return conversion

def toEnglish(D):
    
    conversion = ''
    words = D.split()
    vowels="AEIOUaeiou"
    consonants=''
    
    for word in words:
        if word.find('w') != -1:
            conversion+= word[:word.find('w')] + ' '
        else:
            word=word.replace('ay','')
            conversion+= word[word.rfind('a')+1:] + word[:word.rfind('a')] + ' '
            
    return conversion