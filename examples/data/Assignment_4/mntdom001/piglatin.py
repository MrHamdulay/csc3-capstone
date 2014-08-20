# piglatin.py
# Dominic Manthoko
# 01 April 2014

def toPigLatin(s):
    """ This function converts text written in plain English to piglatin"""
    
    piglatin = []
    sentence_list = s.split()
    #print(sentence_list)
    # loop through each word in the text and convert each word to its piglatin equivalent
    for c in range(len(sentence_list)):
        word = sentence_list[c]
        if word[:1] in 'aeiou':
            #print(y)
            piglatin.append(word[:] +'way')
        else:
            count = 0
            for c in word:
                if c not in 'aeiou':
                    if count==len(word)-1:
                        piglatin.append("a" + word + "ay") 
                    count +=1
                else:
                    piglatin.append(word[count:] + "a" + word[:count] + "ay")
                    break
                    
    message = " ".join(piglatin)
    return message

def toEnglish(s):
    """ This function converts text written in Pig Latin back to English"""
    
    English = []
    new_list = s.split()
    #print(new_list)
    for i in range(len(new_list)):
        word = new_list[i]
        #print(word)
        if word[-3:] == "way":
            English.append(word[:(len(word)-3)])
        else:
            new_string = word[:len(word)-2]
            x = new_string.rfind('a')
            English.append(new_string[x+1:]+new_string[:x])
    
    message = " ".join(English)        
    return message
            
            
        
        