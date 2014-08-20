def toPigLatin(s):
 return (translate(s))
 	
def findFirstVowel(given_word):
 '''Returns the location of the first vowel in the given word.'''
 for i in range(len(given_word)):
  if checkVowel(given_word[i]) == True:
   return i

def translateWord(input_string):
    '''Translates the word and returns the translation to the caller.'''
    firstVowel = findFirstVowel(input_string)
    if firstVowel == None:
        translated = ('a' + input_string + "ay")
    elif firstVowel == 0:
        translated = (input_string + "way")
    elif firstVowel >= 1:
        translated = (input_string[firstVowel:] + 'a' + input_string[:firstVowel] + "ay")
    else:
        translate = ('a' + input_string + 'ay')
    return translated

def translate(inputWords):
    '''Accepts multiple words (separated by spaces) and will return the entire translated phrase.'''
    wordList = inputWords.split()
    translatedString = str()
    for word in range(len(wordList)):
        translatedString = (translatedString + translateWord(wordList[word]) + " ")
    return translatedString

def checkVowel(char):
    '''Returns "True" if submitted charecter is a vowel.'''
    vowels="AaEeIiOoUu"
    for vowel_test in vowels:
        if char == vowel_test:
            return True
    return False
 
   
def toEnglish(s):
    # MUST use a space between the quotations
    words = s.split(" ") ; # split based on space character
    for word in words:
        if word[-3:] == 'way':
            qq = word[:-3]
            return qq
            
        
            
        elif word[-3:] != 'way':
            x = word[:-2]
            y = x[::-1]
            z = y.index('a')
            a = y[:z]
            d = a[::-1]
            b = y[z+1:]
            rr = b[::-1]
            k = d+rr
            return k
