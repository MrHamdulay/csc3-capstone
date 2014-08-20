# Name: Yonela Ford
# Student Number: FRDYON001
# Date: 30 March 2014
# Making a new language

def toPigLatin(s):
    # split the text
    words = s.split()

    # for each word in the line:
    result=""
    for word in words:
        if word[0]=="a" or word[0]=="e" or word[0]=="i" or word[0]=="o" or word[0]=="u":
            result+=word+"way " #all words starting in vowels will just get string "way" added onto them
        #for words starting with consonants:
        else:
            j=0
            x=word+"a"
            for i in word:
                if i!="a" or i!="e" or i!="o" or i!="u" or i!="i":
                    if i=="a" or i=="e" or i=="o" or i=="i" or i=="u": break
                y=x[j+1:]+x[0]
                        
                x=y #each consonant is shitfed to the end and new word evaluated
            result+=x+"ay "
    #return all strings                                  
    return result        
          

def toEnglish(s):
    #split the text
    words=s.split()
    result=""
    #consider each word
    for word in words:
        y=len(word)-2
        new_word=word[:y] #remove "ay" from every word
        
        if new_word[-1]=="w":
            result+=new_word[:-1]+" " #remove"w" from vowels
        else:
            for i in new_word:
                if new_word[-1]=="a": 
                    result+=new_word[:-1]+" "
                    break
                else:
                    x=new_word[-1]+new_word[:-1]
                    new_word=x
    
    return result
        
