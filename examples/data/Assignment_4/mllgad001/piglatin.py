def toPigLatin(s): 
    vowels = "aeiou" 
    n_word = '' 
    
    word_count = 1
    for i in range(len(s)):
        if s[i] == ' ':
            word_count = word_count + 1
    string = s.split(' ') 
    
    # add "way" to words that start with a vowel.
    for i in range(word_count):
        
        word = string[i]
        if word[0] in vowels:
            word = word + 'way'
            
    # add "a" and move first consonant cluster to end and add "ay" 
        else:
            m =0
            for k in word:
                if k not in vowels:
                    m +=1
                else: break
            word = word[m:] + 'a' + word[:m] + 'ay' 

        n_word = n_word + word + ' '
 
    return n_word

def toEnglish(s):
    string = s.split()
    english = ''
    for word in range(len(string)):
        if string[word][-3:] == 'way':
            english = english + string[word][:-3] + ' '
        elif string[word][-2:] == 'ay':
            new_word  = string[word][:-2]
            x =new_word.rfind("a")
            english = english + new_word[x+1:] + new_word[:x] + " "
    return english
  