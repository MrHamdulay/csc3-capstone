'''Pig latin to english converter
Author:Raees Eland
02 April 2014'''

'''converts individual words in an english sentence to pig latin'''
def convert_word(word):
    Vowels = ('a','e','i','o','u','A','E','O','I','U')
    if word[0] in Vowels:  
        return word + "way"     
    else:
        word=word+'a'
        while word[0] not in Vowels:
            word=word[1:]+word[:1]
            if word[0] in Vowels:
                word=word+'ay'
        return word
    
'''returns the english sentence in pig latin'''   
def toPigLatin(s):
    words = s.split(' ')
    sentence = ""   
    for word in words:
        sentence = sentence + convert_word(word)    
        sentence = sentence + " "   
    return sentence

'''converts individual pig latin words to english'''
def convert_toEnglish(s):
    word=s.split(' ')
    for i in word:
        if i[:len(i)-4:-1]=='yaw':
            i=i[:len(i)-3]
        else:
            i=i[:len(i)-2]
            while i[len(i)-1]!='a':
                i=i[len(i)-1]+i[:len(i)-1]
            i=i[:len(i)-1]
        return i
    
'''returns a pig latin sentence in english'''               
def toEnglish(s):
    words = s.split(' ')
    sentence = ""   
    for s in words:
        sentence = sentence + convert_toEnglish(s)    
        sentence = sentence + " "   
    return sentence    